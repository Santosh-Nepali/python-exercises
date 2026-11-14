/* Write a program that asks the user for numbers until the user gives zero. The given numbers are printed in the console from the largest to the smallest. (2p) */
"use strict";
let numbers=[];
/* Intering the numbers in the array */
function userValue(){
    while(true){
        let number=parseInt(prompt("Enter the number"));
        if(number==0){
            break;
        }
        numbers.push(number);
    }
    console.log(`The numbers in the list :: ${numbers}`);
    /* Displaying numbers before Sorting the values  */
    for(let n of numbers){
        document.querySelector("#beforeSorting").innerHTML+=`<br>${n} <br>`;
}
}
/* Sorting the numbers */
function sortingNumbers(){
    numbers.sort((a, b)=>b-a);
    console.log(numbers);
    /* displaying after sorting the numbers */
    for(let n of numbers){
    document.querySelector("#afterSorting").innerHTML+=`<br>${n}<br>`;
}
}
/* calling function for user entering the number until 0 is not enter  */
userValue();
/* Sorting the numbers in descending order */
sortingNumbers();
