"use strict";
let num=[];
for(let n=0; n<5; n++)
{
    num[n]=Number(prompt("Enter the number"));
    console.log(num[n]);
    document.getElementById("userInput").innerHTML+=`${num[n]}<br>`;
}
for(let n=4; n>=0;n--)
{
    console.log(num[n]);
    document.getElementById("reverseOrder").innerHTML+=`${num[n]}<br>`;
}
