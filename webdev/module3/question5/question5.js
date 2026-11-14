"use strict";
let numbers=[];// Global Variables 
function getNumbers(){
    while(true){
        let number=parseInt(prompt("Enter the number"));
        if(numbers.includes(number))
            break;
        numbers.push(number);
}
console.log(numbers);
document.querySelector("#beforeSorting").innerHTML=`<h2>Before Sorting Numbers</h2>`
for(let n of numbers){
    document.querySelector("#beforeSorting").innerHTML+=`<h2><br>${n}</h2>`;
}
}

function sortNumbers(){
    numbers.sort((a,b)=>a-b);
    console.log(numbers);
    document.querySelector("#afterSorting").innerHTML=`<h2>After Sorting Numbers</h2>`
    for(let n of numbers){
        document.querySelector("#afterSorting").innerHTML+=`<h2><br>${n}</h2>`;
    }
    
}

getNumbers();
sortNumbers();

