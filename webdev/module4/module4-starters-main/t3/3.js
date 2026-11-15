'use strict';
const names = ['John', 'Paul', 'Jones'];

// Accessing ElementInternals
let target=document.getElementById("target");

// using for loop in input the value of names

for( let i=0; i<names.length; i++)
{
    target.innerHTML+=`<li> ${names[i]}</li>`;
}
