/* Javascript code for squaroot calculator */
"use strict";

function drCalculator(){
    const num=document.getElementById("value1").value;
    console.log(num);
    if(num==""){
        document.querySelector(".result").innerHTML=`User entered empty value`;
    }
    else if(isNaN(num)){
        document.querySelector(".result").innerHTML=`${num} is not a number`;
    }
    else if(num<0){
        document.querySelector(".result").innerHTML=`${num} is a negative number`;
    }
    else
    {
        let sum=0;
        const max=6;
        const min=1;
        for(let count=0; count<num; count++)
            {
                let randomValue=Math.floor(Math.random()*max)+min;
                console.log(randomValue);
                sum=sum+randomValue;
        }
        document.querySelector(".result").innerHTML=`The sum of random values from ${num} Dices is :: ${sum}`;

    }

}