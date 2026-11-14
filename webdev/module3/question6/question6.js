"use strict";
function randomGenerator(){
    
    let randomNumber=Math.floor(Math.random()*6)+1;
    return randomNumber;

}

function rollingDice(){
    const rollingValue=document.querySelector("#rollingResult");
    let diceValue="";
    //Clearing the previous results
    rollingValue.innerHTML="";

    while(diceValue!=6){
        diceValue=randomGenerator();
        console.log(`${diceValue}`);
        rollingValue.innerHTML+=`<br><li> ${diceValue}</li>`;
    }   
}
