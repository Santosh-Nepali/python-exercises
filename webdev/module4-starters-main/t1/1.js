"use strict";

// Select the element with id="target"
const target=document.getElementById("target");

// Add HTML elements using innerHTML
target.innerHTML = `
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>`;

// Add class "my-list" to the target element
target.classList.add("my-list");