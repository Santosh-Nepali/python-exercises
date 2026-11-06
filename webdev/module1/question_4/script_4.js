/* 
To find the value between the range
Math.floor(Math.random()*max_number)+mini_number 

*/
"use strict";

function randomGenerator(maxNumber, minNumber){
    const num=Math.floor(Math.random()*maxNumber)+minNumber;
    console.log(num);
    return(num);
}
const name=prompt("What is your Name :: ");
const maxNumber=4;
const minNumber=1;
let randomizer=randomGenerator(maxNumber, minNumber);
switch(randomizer){
    case 1:
        document.querySelector("p").innerHTML=`${name}, you are Gryffindor.`;
        break;
    case 2:
        document.querySelector("p").innerHTML=`${name}, you are Slytherin.`;
        break;
    case 3:
        document.querySelector("p").innerHTML=`${name}, you are Hufflepuff.`;
        break;
    case 4:
        document.querySelector("p").innerHTML=`${name}, you are Ravenclaw.`;
        break;
    default:
        document.querySelector("p").innerHTML=`${name}, Not a valid case.`;
}
