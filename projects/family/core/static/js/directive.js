
'use strict';

var directives = angular.module('directives', []);

/***

Открытие модальных окон

*/

directives.directive('modal', function () {
    return {
      template: '<div class="modal fade bs-{{ cls }}">' +
          '<div class="modal-dialog {{ cls }}">' +
            '<div class="modal-content">' + 
              '<div class="modal-header">' + 
                '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>' + 
                '<h4 class="modal-title">{{ title }}</h4>' + 
              '</div>' + 
              '<div class="modal-body" ng-transclude></div>' + 
            '</div>' + 
          '</div>' + 
        '</div>',
      restrict: 'E',
      transclude: true,
      replace:true,
      scope:true,
      link: function postLink(scope, element, attrs) {
        scope.title = attrs.title;
        scope.cls = attrs.cls;

        scope.$watch(attrs.visible, function(value){
          if(value == true)
            $(element).modal('show');
          else
            $(element).modal('hide');
        });

        $(element).on('shown.bs.modal', function(){
          scope.$apply(function(){
            scope.$parent[attrs.visible] = true;
          });
        });

        $(element).on('hidden.bs.modal', function(){
          scope.$apply(function(){
            scope.$parent[attrs.visible] = false;
          });
        });
      }
    };
  });

/* Костылизация для вывода значений в ангуляре */

directives.directive('ngInitial', function($parse) {
        return{
    restrict: 'A',
    controller: ['$scope', '$element', '$attrs', '$parse', function($scope, $element, $attrs, $parse){

      var getter, setter, val, tag;
      tag = $element[0].tagName.toLowerCase();

      val = $attrs.initialValue || $element.val();
      if(tag === 'input'){
        if($element.attr('type') === 'checkbox'){
          val = $element[0].checked ? true : undefined;
        } else if($element.attr('type') === 'radio'){
          val = ($element[0].checked || $element.attr('selected') !== undefined) ? $element.val() : undefined;
        } 
      }

      if($attrs.ngModel){
        getter = $parse($attrs.ngModel);
        setter = getter.assign;
        setter($scope, val);
      }
    }]
  };
});

/***

Переключение между табами (сейчас не используется)

*/

directives.directive('showtab',
    function () {
        return {
            link: function (scope, element, attrs) {
                element.click(function(e) {
                    e.preventDefault();
                    $(element).tab('show');
                });
            }
        };
    });

directives.directive('datepicker',
    function () {
        return {
            link: function (scope, element, attrs) {
                $(element).datepicker({
                      language: 'ru',
                      format: 'yyyy-mm-dd'

                });
            }
        };
    });

directives.directive('input', [function() {
    return {
        restrict: 'E',
        require: '?ngModel',
        link: function(scope, element, attrs, ngModel) {
            if (
                   'undefined' !== typeof attrs.type
                && 'number' === attrs.type
                && ngModel
            ) {
                ngModel.$formatters.push(function(modelValue) {
                    return Number(modelValue);
                });

                ngModel.$parsers.push(function(viewValue) {
                    return Number(viewValue);
                });
            }
        }
    }
}]);

/***

Эта директива позволяет встраивать в DOM html через $http 

*/

directives.directive('bindUnsafeHtml', ['$compile', function ($compile) {
      return function(scope, element, attrs) {
          scope.$watch(
            function(scope) {
              // watch the 'bindUnsafeHtml' expression for changes
              return scope.$eval(attrs.bindUnsafeHtml);
            },
            function(value) {
              // when the 'bindUnsafeHtml' expression changes
              // assign it into the current DOM
              element.html(value);

              // compile the new DOM and link it to the current
              // scope.
              // NOTE: we only compile .childNodes so that
              // we don't get into infinite loop compiling ourselves
              $compile(element.contents())(scope);
            }
        );
    };

}]);

directives.directive('elastic', [
    '$timeout',
    function($timeout) {
        return {
            restrict: 'A',
            link: function($scope, element) {
                $scope.initialHeight = $scope.initialHeight || element[0].style.height;
                var resize = function() {
                    element[0].style.height = $scope.initialHeight;
                    element[0].style.height = "" + element[0].scrollHeight + "px";
                };
                element.on("input change", resize);
                $timeout(resize, 0);
            }
        };
    }
]);

directives.directive('showErrors', function() {
    return {
      restrict: 'A',
      require:  '^form',
      link: function (scope, el, attrs, formCtrl) {
        // find the text box element, which has the 'name' attribute
        var inputEl   = el[0].querySelector("[name]");
        // convert the native text box element to an angular element
        var inputNgEl = angular.element(inputEl);
        // get the name on the text box so we know the property to check
        // on the form controller
        var inputName = inputNgEl.attr('name');

        // only apply the has-error class after the user leaves the text box
        inputNgEl.bind('blur', function() {
          el.toggleClass('has-error', formCtrl[inputName].$invalid);
        })
      }
    }
  });


angular.module('pdf', []).directive('ngPdf', [ '$window', function($window) {
    var backingScale = function(canvas) {
      var ctx = canvas.getContext('2d');
      var dpr = window.devicePixelRatio || 1;
      var bsr = ctx.webkitBackingStorePixelRatio ||
        ctx.mozBackingStorePixelRatio ||
        ctx.msBackingStorePixelRatio ||
        ctx.oBackingStorePixelRatio ||
        ctx.backingStorePixelRatio || 1;

      return dpr / bsr;
    };

    var setCanvasDimensions = function(canvas, w, h) {
      var ratio = backingScale(canvas);
      canvas.width = Math.floor(w * ratio);
      canvas.height = Math.floor(h * ratio);
      canvas.style.width = Math.floor(w) + 'px';
      canvas.style.height = Math.floor(h) + 'px';
      canvas.getContext('2d').setTransform(ratio, 0, 0, ratio, 0, 0);
      return canvas;
    };
    return {
      restrict: 'E',
      templateUrl: function(element, attr) {
        return attr.templateUrl ? attr.templateUrl : 'partials/viewer.html'
      },
      link: function(scope, element, attrs) {
        var url = scope.pdfUrl;
        var pdfDoc = null
        var pageNum = (attrs.page ? attrs.page : 1);
        var scale = attrs.scale > 0 ? attrs.scale : 1;
        var canvas = (attrs.canvasid ? document.getElementById(attrs.canvasid) : document.getElementById('pdf-canvas'));
        var ctx = canvas.getContext('2d');
        var windowEl = angular.element($window);

        windowEl.on('scroll', function() {
          scope.$apply(function() {
            scope.scroll = windowEl[0].scrollY;
          });
        });

        PDFJS.disableWorker = true;
        scope.pageNum = pageNum;

        scope.renderPage = function(num) {
          pdfDoc.getPage(num).then(function(page) {
            var viewport;
            var pageWidthScale;
            var pageHeightScale;
            var renderContext = {};
            var pageRendering;

            if (attrs.scale === 'page-fit' && !scale) {
              viewport = page.getViewport(1);
              pageWidthScale = element[0].clientWidth / viewport.width;
              pageHeightScale = element[0].clientHeight / viewport.height;
              scale = Math.min(pageWidthScale, pageHeightScale);
            } else {
              viewport = page.getViewport(scale)
            }

            setCanvasDimensions(canvas, viewport.width, viewport.height);

            renderContext = {
              canvasContext: ctx,
              viewport: viewport
            };

            page.render(renderContext).promise.then(function() {
              if (typeof scope.onPageRender === 'function' ) {
                scope.onPageRender();
              }
            });
          });
        };

        scope.goPrevious = function() {
          if (scope.pageToDisplay <= 1) {
            return;
          }
          scope.pageNum = parseInt(scope.pageNum) - 1;
        };

        scope.goNext = function() {
          if (scope.pageToDisplay >= pdfDoc.numPages) {
            return;
          }
          scope.pageNum = parseInt(scope.pageNum) + 1;
        };

        scope.zoomIn = function() {
          scale = parseFloat(scale) + 0.2;
          scope.renderPage(scope.pageToDisplay);
          return scale;
        };

        scope.zoomOut = function() {
          scale = parseFloat(scale) - 0.2;
          scope.renderPage(scope.pageToDisplay);
          return scale;
        };

        scope.changePage = function() {
          scope.renderPage(scope.pageToDisplay);
        };

        scope.rotate = function() {
          if (canvas.getAttribute('class') === 'rotate0') {
            canvas.setAttribute('class', 'rotate90');
          } else if (canvas.getAttribute('class') === 'rotate90') {
            canvas.setAttribute('class', 'rotate180');
          } else if (canvas.getAttribute('class') === 'rotate180') {
            canvas.setAttribute('class', 'rotate270');
          } else {
            canvas.setAttribute('class', 'rotate0');
          }
        };

        function renderPDF() {
          if (url && url.length) {
            PDFJS.getDocument(url, null, null, scope.onProgress).then(
                function(_pdfDoc) {
                  if (typeof scope.onLoad === 'function') {
                    scope.onLoad();
                  }

                  pdfDoc = _pdfDoc;
                  scope.renderPage(scope.pageToDisplay);

                  scope.$apply(function() {
                    scope.pageCount = _pdfDoc.numPages;
                  });
                }, function(error) {
                  if (error) {
                    if (typeof scope.onError === 'function') {
                      scope.onError(error);
                    }
                  }
                }
            );
          }
        }

        scope.$watch('pageNum', function(newVal) {
          scope.pageToDisplay = parseInt(newVal);
          if (pdfDoc !== null) {
            scope.renderPage(scope.pageToDisplay);
          }
        });

        scope.$watch('pdfUrl', function(newVal) {
          if (newVal !== '') {
            console.log('pdfUrl value change detected: ', scope.pdfUrl);
            url = newVal;
            scope.pageToDisplay = 1;
            renderPDF();
          }
        });

      }
    };
  } ]);

