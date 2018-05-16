'use strict';

var putPoint = function(e){
    context.arc();
};

$(document).ready(function(){
    var canvas = $('#canvas').get(0);
    var context = canvas.getContext('2d');
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    canvas.addEventListener('mousedown', putPoint);
});