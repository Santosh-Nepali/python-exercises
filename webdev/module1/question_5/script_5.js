/* 
To find the value between the range
Math.floor(Math.random()*max_number)+mini_number 

*/
"use strict";
function checkYear(){
    let year_value=parseInt(document.getElementById("year").value);
    console.log(year_value)
    if(year_value%400==0)
        document.querySelector(".resultShow").innerHTML=`${year_value} is a leap year.`;
    else if(year_value%100==0)
        document.querySelector(".resultShow").innerHTML=`${year_value} is not a leap year.`;
    else if(year_value%4==0)
        document.querySelector(".resultShow").innerHTML=`${year_value} is a Leap year.`;
    else
        document.querySelector(".resultShow").innerHTML=`${year_value} is not a leap year.`;
}