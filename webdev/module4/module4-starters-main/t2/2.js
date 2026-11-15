"use strict";

// Select the target element
const target = document.getElementById("target");

// Create first list item
const firstItem = document.createElement("li");
firstItem.textContent = "First item";

// Create second list item
const secondItem = document.createElement("li");
secondItem.textContent = "Second item";


// Create third list item
const thirdItem = document.createElement("li");
thirdItem.textContent = "Third item";


// Add class to the second list item
secondItem.classList.add("my-item");


// Append all list items to the target
target.appendChild(firstItem);
target.appendChild(secondItem);
target.appendChild(thirdItem);