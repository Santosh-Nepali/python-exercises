"use strict";
// Accessing the html elements
let trigger=document.getElementById("trigger");
let target=document.getElementById("target");

//defining event for mouseenter events
trigger.addEventListener("mouseenter", function(){
    target.src="img/picB.jpg";
});

// Defining event for mouse leave 
trigger.addEventListener("mouseleave", function(){
    target.src="img/picA.jpg";
});