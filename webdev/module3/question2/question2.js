/* 
Write a program that asks the user for the number of participants. After this, the program asks for the names of all participants. Finally, the program prints the names of the participants on the web page in an ordered list (<ol>) in alphabetical order. (2p) */

"use strict";
let nameOfParticipants=[];

function startOfProgram(){
    let totalPerson=Number(document.getElementById("totalPerson").value);
    console.log(totalPerson);
    document.querySelector("#participantList").innerHTML=``;
    if (totalPerson<=0){
        document.querySelector("#participantList").innerHTML=`${totalPerson} You have enter invalid data.`;
    }
    else{
        /* This will disable the  button of submit */
        const submitButton=document.querySelector("#submit");
        submitButton.disabled=true;
        submitButton.textContent="submitted";
        for(let counter=1; counter<=totalPerson; counter++){
            document.querySelector("#participantList").innerHTML+=`
            <label for =".nameList">Enter Name: </label>
            <input type="text" class="nameList" placeholder="enter name">
            <br> <br>
            `
        }
        document.querySelector("#participantList").innerHTML+=`
        <input type="button" id="addName" value="Add Name" onclick="addName()"> 
        `
    }
}

function addName(){
    nameOfParticipants=[];
    let inputs=document.querySelectorAll(".nameList");
    let addNameButton=document.querySelector("#addName");
    addNameButton.disabled=true;
    for(let input of inputs){
        console.log(input.value);
        let eachValue=input.value.trim();
        if(eachValue!==""){
            nameOfParticipants.push(eachValue);
        }
    }
    nameOfParticipants.sort((a, b)=>a.localeCompare(b));
    console.log(nameOfParticipants);
    let output="<ol>";
    for(let eachParticipant of nameOfParticipants){
        output+=`<li>${eachParticipant}</li>`;
    }
    output+="</ol>"
    document.querySelector("#participantList").innerHTML+=output;
}