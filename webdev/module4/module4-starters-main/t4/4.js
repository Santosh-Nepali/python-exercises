'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
// Select the target element
const target = document.getElementById("target");

// Loop through students array
for (let i = 0; i < students.length; i++) {

    // Create option element
    const option = document.createElement("option");

    // Add student number as value
    option.value = students[i].id;

    // Add student name as text
    option.textContent = students[i].name;

    // Append option to select element
    target.appendChild(option);
}