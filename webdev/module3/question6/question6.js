"use strict";
function rollingDice(){
    let diceValue="";
    const rollingValue=document.querySelector("#rollingResult");
    diceValue=Math.floor(Math.random()*6)+1;
    do{
        console.log(`${diceValue}`);
        rollingValue.innerHTML+=`<br><li> ${diceValue}</li>`;
    }while(diceValue!=6);   
}

rollingDice();