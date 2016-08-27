'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/view1', {
        templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
    });
}])

.controller('View1Ctrl', ['$scope', '$http', function($scope, $http) {
    $http.get("https://api.tuchfarber.com/api/test")
    .then(function(response) {
        $scope.content = response.data;
        $scope.statuscode = response.status;
        $scope.statustext = response.statustext;
    })
}]);
