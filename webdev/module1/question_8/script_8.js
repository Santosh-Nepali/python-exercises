/* 
To find the value between the range
Math.floor(Math.random()*max_number)+mini_number 

*/
"use strict";
function checkYear(){
    let firstYear=parseInt(document.getElementById("firstYear").value);
    console.log(firstYear);
    let endYear=parseInt(document.getElementById("endYear").value);
    console.log(endYear);
    document.querySelector(".resultShow").innerHTML = "";/* clear the previous results */
    while(firstYear<=endYear){
        if(firstYear%400==0)
            document.querySelector(".resultShow").innerHTML+=`<li> ${firstYear}=leap year. </li>`;
        else if(firstYear%100==0)
            document.querySelector(".resultShow").innerHTML+=`<li> ${firstYear} = not a leap year. </li>`;
        else if(firstYear%4==0)
            document.querySelector(".resultShow").innerHTML+=`<li> ${firstYear} =  Leap year. </li>`;
        else
            document.querySelector(".resultShow").innerHTML+=`<li> ${firstYear} = not a leap year. </li>`;
        firstYear++;
        }   
}