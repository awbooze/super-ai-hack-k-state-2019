
// https://stackoverflow.com/questions/19840907/draw-rectangle-over-html-with-javascript
//You can create a canvas element and place it on top of the HTML page:

$(document).ready(function () {
    $('.map').maphilight();
});   

var img = document.getElementById('svg'); 
img.onload = function() {
// write dimensions to html page
document.getElementById("dimensions").innerHTML = this.width + 'x' + this.height;
}

var body = document.getElementsByTagName('body')[0];
var map = body.getElementsByTagName('map')[0];

newArea = document.createElement('area');
newArea.shape = 'rect';
newArea.coords = '0,0,100,100';
newArea.href = 'https://google.com/';
map.appendChild(newArea)

