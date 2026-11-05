"use strict";
function addition(firstNum, secondNum, thirdNum){
    return(firstNum+secondNum+thirdNum);
}
function product(firstNum, secondNum, thirdNum){
    return(firstNum*secondNum*thirdNum);
}
function average(firstNum, secondNum, thirdNum){
    return((firstNum+secondNum+thirdNum)/3.0);

}

const firstNum=parseFloat(prompt("Enter First Number :: "));
const secondNum=parseFloat(prompt("Enter the second number :: "));
const thirdNum=parseFloat(prompt("Enter the third number :: "));
if(Number.isNaN(firstNum) || Number.isNaN(secondNum) || Number.isNaN(thirdNum)){
    document.querySelector("#invalidData").textContent=`Please enter the valid numbers. `;
}
else{
    document.querySelector("#additionValue").innerHTML=`The addition of ${firstNum} + ${secondNum} + ${thirdNum} is ${addition(firstNum, secondNum, thirdNum)}.`;
    document.querySelector("#productValue").innerHTML=`The product of ${firstNum} * ${secondNum} * ${thirdNum} is ${product(firstNum, secondNum, thirdNum)}.`;
    document.querySelector("#averageValue").innerHTML=`The average of ${firstNum}, ${secondNum} and ${thirdNum} is ${average(firstNum, secondNum, thirdNum)}.`; 
    console.log(addition(firstNum,secondNum,thirdNum))
}


