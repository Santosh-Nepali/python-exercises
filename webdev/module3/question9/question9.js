"use strict";

//Defining empty array
let numArray=[];
let evenListArray=[];

// Accessing all the elements of html elements
let numBox=document.getElementById("numBox");
let addNum=document.getElementById("addNum");
let finnishBtn=document.getElementById("finnishBtn");
let originalArray=document.getElementById("originalArray");
let evenArray=document.getElementById("evenArray");
let message=document.getElementById("message");

//register users enter value
addNum.addEventListener("click", function(){
    let eachNum=numBox.value.trim();
    if(eachNum==""){
        message.textContent="Please Enter numbers.";
        return;
    }
    numArray.push(eachNum);
    console.log(numArray);

//clearing the values 
numBox.textContent="";
numBox.focus();
message.textContent="";
});

// action after lopeta
finnishBtn.addEventListener("click", function(){
    evenListArray=even(numArray);

    // hiding lopeta but unhiding even and original button
    finnishBtn.hidden=true;
    originalArray.hidden=false;
    evenArray.hidden=false;
    addNum.hidden=true;
    
    //clearing the values 
    numBox.textContent="";
    numBox.focus();
});

//function for arranging only even number array
function even(numArray){
    let newEvenArray=[];

    for(let each of numArray){
        if(each%2==0){
            newEvenArray.push(each);
        }

    }
    return newEvenArray;
}

// original Array list 
originalArray.addEventListener("click", function(){
    /* document.getElementById("original").textContent=`${numArray}` */
    for(let each of numArray){
        document.querySelector("#original").innerHTML+=`<br>${each}`;
        }
    });

evenArray.addEventListener("click", function(){
    /* document.getElementById("#even").textContent=`${evenListArray}`;
      */   
    for( let each of evenListArray){
        document.querySelector("#even").innerHTML+=`<br>${each}`;
        } 
      
    });
