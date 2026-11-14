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
    for(let n of numbers){
        document.querySelector("#beforeSorting").innerHTML+=`<br>${n} <br>`;
}
}
/* Sorting the numbers */
function sortingNumbers(){
    for(let i=0;i<numbers.length;i++){
        for(let j=0;j<numbers.length-i-1;j++){
            if(numbers[j]<numbers[j+1]){
                let temp=numbers[j];
                numbers[j]=numbers[j+1];
                numbers[j+1]=temp;
            }
    }
}
console.log(numbers);
for(let n of numbers){
    document.querySelector("#afterSorting").innerHTML+=`<br>${n}<br>`;
}
}
/* calling function for user entering the number until 0 is not enter  */
userValue();
/* Sorting the numbers in descending order */
sortingNumbers();
