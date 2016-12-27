/*global angular*/
angular.module('ymaps', [])
.factory('$script', ['$q', '$rootScope', function ($q, $rootScope) {
    "use strict";
    //классический кроссбраузерный способ подключить внешний скрипт
    function loadScript(path, callback) {
        var el = document.createElement("script");
        el.onload = el.onreadystatechange = function () {
            if (el.readyState && el.readyState !== "complete" &&
                el.readyState !== "loaded") {
                return;
            }
            // если все загрузилось, то снимаем обработчик и выбрасываем callback
            el.onload = el.onreadystatechange = null;
            if(angular.isFunction(callback)) {
                callback();
            }
        };
        el.async = true;
        el.src = path;
        document.getElementsByTagName('body')[0].appendChild(el);
    }
    var loadHistory = [], //кэш загруженных файлов
        pendingPromises = {}; //обещания на текущие загруки
    return function(url) {
        var deferred = $q.defer();
        if(loadHistory.indexOf(url) !== -1) {
            deferred.resolve();
        }
        else if(pendingPromises[url]) {
            return pendingPromises[url];
        } else {
            loadScript(url, function() {
                delete pendingPromises[url];
                loadHistory.push(url);
                //обязательно использовать `$apply`, чтобы сообщить
                //angular о том, что что-то произошло
                $rootScope.$apply(function() {
                    deferred.resolve();
                });
            });
            pendingPromises[url] = deferred.promise;
        }
        return deferred.promise;
    };
}])
.factory('ymapsLoader', ['$window', '$timeout', '$script', 'ymapsConfig', function($window, $timeout, $script, ymapsConfig) {
    "use strict";
    var scriptPromise;
    return {
        ready: function(callback) {
            if(!scriptPromise) {
                scriptPromise = $script(ymapsConfig.apiUrl).then(function() {
                    return $window.ymaps;
                });
            }
            scriptPromise.then(function(ymaps) {
                ymaps.ready(function() {
                    $timeout(function() {callback(ymaps);});
                });
            });
        }
    };
}])
.constant('ymapsConfig', {
    apiUrl: '//api-maps.yandex.ru/2.1/?load=package.standard,package.clusters&mode=release&lang=ru-RU&ns=ymaps',
    mapBehaviors: ['default'],
    markerOptions: {
        preset: 'islands#darkgreenIcon'
    },
    fitMarkers: true // Если поменять, то будет сбрасывать масштаб при добавлении меток
})
.value('debounce', function (func, wait) {
    "use strict";
    var timeout = null;
    return function () {
        var context = this, args = arguments;
        var later = function () {
            timeout = null;
            func.apply(context, args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
})
.controller('YmapController', ['$scope', '$element', 'ymapsLoader', 'ymapsConfig', 'debounce', function ($scope, $element, ymapsLoader, config, debounce) {
    "use strict";
    function initAutoFit(map, collection) {
        //brought from underscore http://underscorejs.org/#debounce
        var markerMargin = 0.1,
            fitMarkers = debounce(function () {
                if(collection.getLength() > 0) {
                    var bounds = collection.getBounds(),
                    //make some margins from
                        topRight = [
                            bounds[1][0] + markerMargin,
                            bounds[1][1] + markerMargin
                        ],
                        bottomLeft = [
                            bounds[0][0] - markerMargin,
                            bounds[0][1] - markerMargin
                        ];
                    map.setBounds([bottomLeft, topRight], {checkZoomRange: true});
                }
            }, 100);
        collection.events.add('boundschange', fitMarkers);
    }
    var self = this;
    ymapsLoader.ready(function(ymaps) {
        self.addMarker = function(coordinates, properties, options) {
            console.log(coordinates)
            var placeMark = new ymaps.Placemark(coordinates, properties, options);
            $scope.geoObjects.push(placeMark);
            self.clusterer.add($scope.geoObjects);
            self.map.geoObjects.add(self.clusterer);
            self.map.setBounds(self.clusterer.getBounds(), {checkZoomRange: true});
            return placeMark;
        };
        self.removeMarker = function (marker) {
            $scope.geoObjects.splice($scope.geoObjects.indexOf(marker),1);
            self.clusterer.remove(marker);
            self.map.setBounds(self.clusterer.getBounds(), {checkZoomRange: true});
        };
        self.map = new ymaps.Map($element[0], {
            center   : $scope.center || [0, 0],
            zoom     : $scope.zoom || 0,
            behaviors: config.mapBehaviors,
            controls: []
        });

        self.clusterer = new ymaps.Clusterer({
            preset: 'islands#invertedVioletClusterIcons',
            groupByCoordinates: false,
            clusterDisableClickZoom: false,
            clusterHideIconOnBalloonOpen: false,
            geoObjectHideIconOnBalloonOpen: false
        });
        $scope.geoObjects = []
        $scope.markers = new ymaps.GeoObjectCollection({}, config.markerOptions);

        if(config.fitMarkers) {
            initAutoFit(self.map, $scope.markers);
        }
        var updatingBounds, moving;
       $scope.$watch('center', function(newVal) {
            if(updatingBounds) {
                return;
            }
            moving = true;
            self.map.panTo(newVal).always(function() {
                moving = false;
            });
        }, true);
        $scope.$watch('zoom', function(zoom) {
            if(updatingBounds) {
               return;
            }
            self.map.setZoom(zoom, {checkZoomRange: true});
        });
        self.map.events.add('boundschange', function(event) {
            if(moving) {
                return;
            }
            //noinspection JSUnusedAssignment
            updatingBounds = true;
            $scope.$apply(function() {
                $scope.center = event.get('newCenter');
                $scope.zoom = event.get('newZoom');
            });
            updatingBounds = false;
        });

    });
}])
.directive('yandexMap', ['ymapsLoader', function (ymapsLoader) {
    "use strict";
    return {
        restrict: 'EA',
        terminal: true,
        transclude: true,
        scope: {
            center: '=',
            zoom: '='
        },
        link: function($scope, element, attrs, ctrl, transcludeFn) {
            ymapsLoader.ready(function() {
                transcludeFn(function( copy ) {
                    element.append(copy);
                });
            });
        },
        controller: 'YmapController'
    };
}])
.directive('ymapMarker', function () {
    "use strict";
    return {
        restrict: "EA",
        require : '^yandexMap',
        scope   : {
            coordinates: '=',
            index: '=',
            properties: '=',
            options: '=',
            preset: '='
        },
        link    : function ($scope, elm, attr, mapCtrl) {
            var marker;
            function pickMarker() {
                var coord = [
                    parseFloat($scope.coordinates[0]),
                    parseFloat($scope.coordinates[1])
                ];
                if (marker) {
                    marker.geometry.setCoordinates(coord);
                }
                else {
                    marker = mapCtrl.addMarker(coord, angular.extend({iconContent: $scope.index}, $scope.properties), $scope.options);                }
            }

            $scope.$watch("index", function (newVal) {
                if (marker) {
                    marker.properties.set('iconContent', newVal);
                }
            });

            $scope.$watch("coordinates", function (newVal) {
                if (newVal) {
                    pickMarker();
                }
            }, true);
            $scope.$on('$destroy', function () {
                if (marker) {
                    mapCtrl.removeMarker(marker);
                }
            });
        }
    };
});