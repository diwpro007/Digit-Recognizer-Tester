'use strict';

var putPoint = function(e){
    context.arc();
};

$(document).ready(function(){
	console.log("found");
    var canvas = $('#canvas').get(0);
    var context = canvas.getContext('2d');
    
    canvas.width = 400;
    canvas.height = 400;
    
    canvas.addEventListener('mousedown', putPoint);
});