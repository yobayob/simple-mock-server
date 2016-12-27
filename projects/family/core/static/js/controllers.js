
'use strict';

var controllers = angular.module('controllers', []);


/* Загрузка JSON */
controllers.controller('Data', ['$scope', '$http', function($scope, $http){
  $scope.getData = function(url){
    $http.get(url).success(function(data){
      $scope.data = data;
      console.log(data);
    });
  }
  $scope.sort = function(keyname){
     $scope.orderProp = keyname; 
     $scope.sortReverse = !$scope.sortReverse;
     };
  $scope.getBalloon = function(marker){
    if (marker.site!=null){
      var site = '<p><b>Сайт: </b><a href="'+marker.site+'">'+marker.site+'</a></p>'
    } else {
      var site = ''
    }
    if (marker.phone!=null){
      var phone = '</p><p><b>Телефон: </b>'+ marker.phone + '</p>'
    } else {
      var phone = ''
    }
    return '<p><b>Полное название: </b>'+ marker.full_name+'</p><p><b>Адрес: </b>' + marker.address + phone + site
  }
}])


/*Отправка POST-форм */
controllers.controller('PostForm', ['$scope', '$http', function($scope, $http){
  $scope.form = {};
  $scope.formActive=true;
  $scope.sbm = function(url){
      console.log($scope.form);
    $http({
        url: url,
        method: "POST",
        data: $scope.form
    })
    .then(function(response) {
      if(response.data=='DONE'){
          $scope.formActive = !$scope.formActive;
      } else if(response.data=='RELOAD'){
        document.location.reload(true);
      }
      else{
        $scope.error = response.data;
      }}
    );
  }
}]);


/* Авторизация */
controllers.controller('auth', ['$scope', '$rootScope', '$http', function($scope, $rootScope, $http){
  $rootScope.showModal=false;
	$scope.auth = {}

	$scope.sbm = function() {
		$http({
        url: '/login/',
        method: "POST",
        data: $scope.auth
    })
    .then(function(response) {
    	if(response.data=='OK'){
           document.location.reload(true);
    	}
    }, function(response){

      $scope.error = response.data;
    })
	}

}]);


/* Подгрузка форм */
controllers.controller('Profile', ['$scope', '$http', function($scope, $http){
    $scope.titleModal = "Изменение";
    $scope.getForm = function(url){
        $http.get(url).success(function(data){
        $scope.form = data;
      })
    }

  }]);


/* PDF Viewer */
controllers.controller('DocCtrl', function($scope) {

  $scope.pdfName = 'Relativity: The Special and General Theory by Albert Einstein';
  $scope.getPdf = function(url){
    console.log(url);
    $scope.pdfUrl = url;
  };
  $scope.scroll = 0;
  $scope.loading = 'loading';

  $scope.getNavStyle = function(scroll) {
    if(scroll > 100) return 'pdf-controls fixed';
    else return 'pdf-controls';
  }

  $scope.onError = function(error) {
    console.log(error);
  }

  $scope.onLoad = function() {
    $scope.loading = '';
  }

  $scope.onProgress = function(progress) {
    console.log(progress);
  }

});

/* Добавление клиентов */
controllers.controller('AddPatient', ['$scope', '$http', function($scope, $http){
    $scope.form = {};
    $scope.main = {}
    $scope.patients = [];
    $scope.formActive=true;
    $scope.step_1=true;

    $scope.get_patient_data = function(id) {
        $http.get('/json/patient/' + id).success(function (data) {
            $scope.step_1=false;
            $scope.step_3=true;
            $scope.patient_data =  data.name + ' (ID: ' + data.id + ')';
        });
    }
  }]);
