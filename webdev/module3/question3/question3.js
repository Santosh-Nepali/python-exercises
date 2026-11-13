/*
Write a program that asks for the names of six dogs. 
The program prints dog names to unordered list <ul> in 
reverse alphabetical order. 
 */

"use strict";
let nameOfDogs=[];

function startOfProgram(){
        for(let counter=1; counter<=6; counter++){
            document.querySelector("#dogListReverseOrder").innerHTML+=`
            <label for =".nameList">Enter Name of Dog: </label>
            <input type="text" class="nameList" placeholder="enter name">
            <br> <br>
            `
        }
        document.querySelector("#dogListReverseOrder").innerHTML+=`
        <input type="button" id="addName" value="Add Name" onclick="addName()"> 
        `
    }


function addName(){
    nameOfDogs=[];
    let inputs=document.querySelectorAll(".nameList");
    let addNameButton=document.querySelector("#addName");
    addNameButton.disabled=true;
    for(let input of inputs){
        console.log(input.value);
        let eachValue=input.value.trim();
        if(eachValue!==""){
            nameOfDogs.push(eachValue);
        }
    }
    // sorting the list of name in reverse order
    nameOfDogs.sort((a, b)=>b.localeCompare(a));
    console.log(nameOfDogs);
    let output="<ul>";
    for(let eachDog of nameOfDogs){
        output+=`<li>${eachDog}</li>`;
    }
    output+="</ul>"
    document.querySelector("#dogListReverseOrder").innerHTML+=output;
}

startOfProgram();