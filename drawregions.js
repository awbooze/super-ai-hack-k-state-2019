
// https://stackoverflow.com/questions/19840907/draw-rectangle-over-html-with-javascript
//You can create a canvas element and place it on top of the HTML page:

fetch('Output.txt')
  .then(response => response.text())
  .then(text => console.log(text))
  // outputs the content of the text file


var rooms = []
var img = document.getElementById('svg');
var width = img.naturalWidth;
var height = img.naturalHeight;


function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {

    	formatInput(this.responseText);
    }
  };
  xhttp.open("GET", "Output.txt", true);
  xhttp.send();
}

function formatInput(str){
	res = str.split("\n");
	for (i = 0; i < res.length; i++) { 
		res2 = res[i].split(" ");
		rooms.push([res2[0], (width*res2[1]), (height*res2[2])]);
		//alert(res[i][0]);
	} 
	for(j = 0; j < rooms.length; j++){
		newArea = document.createElement('area');
		newArea.shape = 'circle';
		newArea.coords = rooms[j][1] + ',' + rooms[j][2] + ',40';
		map.appendChild(newArea);
	}
}

$(document).ready(function () {
    $('.map').maphilight();
});  

var body = document.getElementsByTagName('body')[0];
var map = body.getElementsByTagName('map')[0];

// function draw(name, x, y){
// 	var canvas = document.createElement('canvas'); //Create a canvas element
// 	//Set canvas width/height
// 	canvas.style.width='100%';
// 	canvas.style.height='100%';
// 	//Set canvas drawing area width/height
// 	canvas.width = window.innerWidth;
// 	canvas.height = window.innerHeight;
// 	//Position canvas
// 	canvas.style.position='absolute';
// 	canvas.style.left=0;
// 	canvas.style.top=0;
// 	canvas.style.zIndex=100000;
// 	canvas.style.pointerEvents='none'; //Make sure you can click 'through' the canvas
// 	document.body.appendChild(canvas); //Append canvas to body element
// 	var context = canvas.getContext('2d');
// 	//Draw rectangle
// 	context.globalAlpha = 0.3; // set global alpha
// 	context.beginPath();
// 	context.arc(x, y, 20, 0, 2 * Math.PI, false);
// 	context.fillStyle = "purple";
// 	context.fill();
// }

