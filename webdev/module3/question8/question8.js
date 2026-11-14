"use strict";
//Getting HTML elements
const txtBox=document.getElementById("txtBox");
const addBtn=document.getElementById("addBtn");
const finishBtn=document.getElementById("finishBtn");
const message=document.getElementById("message");
const FinalResultTxt=document.getElementById("result");

//defining empty array
  let txtArray=[];

//Adding strings 
addBtn.addEventListener("click", function(){
    let userInput=txtBox.value.trim();
    if(userInput==""){
        document.getElementById("message").textContent="Please enter a string.";
        return;
    }
    txtArray.push(userInput);
    console.log(txtArray);

//clearning input box
    txtBox.value="";
    txtBox.focus();
    message.textContent="";
    FinalResultTxt.textContent="";


});

// Finish button implementation
finishBtn.addEventListener("click",function(){

let concatResult=concat(txtArray);
console.log(concatResult);
document.getElementById("result").textContent=`The Concatenated string is :: ${concatResult}`;

//clearning printed results box
/* ß */


});

//Concatenation Implementation 
function concat(ArrayOfTxt){
    let result=""
    for(let each_string of ArrayOfTxt){
        result+=each_string;
    }
    return result;
}
