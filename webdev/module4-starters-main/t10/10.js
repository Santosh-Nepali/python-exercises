"use strict";

// Access the form
let nameForm = document.querySelector("form");

// Access the target paragraph
let target = document.getElementById("target");

// Add submit event listener
nameForm.addEventListener("submit", function(event) {

    // Stop default form submission
    event.preventDefault();

    // Access input fields using attribute selectors
    let firstName = document.querySelector("input[name='firstname']").value;
    let lastName = document.querySelector("input[name='lastname']").value;

    // Display the result
    target.textContent = `Your name is ${firstName} ${lastName}`;

});