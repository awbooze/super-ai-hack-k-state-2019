
// https://stackoverflow.com/questions/19840907/draw-rectangle-over-html-with-javascript
//You can create a canvas element and place it on top of the HTML page:

fetch('Output.txt')
  .then(response => response.text())
  .then(text => console.log(text))
  // outputs the content of the text file

  

//Position parameters used for drawing the rectangle
var x = 100;
var y = 150;
var width = 200;
var height = 150;

var canvas = document.createElement('canvas'); //Create a canvas element
//Set canvas width/height
canvas.style.width='100%';
canvas.style.height='100%';
//Set canvas drawing area width/height
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
//Position canvas
canvas.style.position='absolute';
canvas.style.left=0;
canvas.style.top=0;
canvas.style.zIndex=100000;
canvas.style.pointerEvents='none'; //Make sure you can click 'through' the canvas
document.body.appendChild(canvas); //Append canvas to body element
var context = canvas.getContext('2d');
//Draw rectangle
context.rect(x, y, width, height);
context.fillStyle = 'yellow';
context.fill();

alert("DOES THIS WORK??")