/* Javascript code for squaroot calculator */
"use strict";
/* asking from user about confirmation of action */
let answer=confirm("Should I calculate the square root?");
/*  console.log(answer);*/
if(answer){
    /* show the calculator section when user selects ok  */
    document.getElementById("calculator").hidden=false;
}
else{ 
        document.getElementById("result").textContent=`The square root is not calculated`;
    }

function srCalculate(){
    const num=parseInt((document.getElementById("value1")).value);
    document.querySelector("p").innerHTML=`The result of square root is ${Math.sqrt(num)}`;
    console.log(num);
    }