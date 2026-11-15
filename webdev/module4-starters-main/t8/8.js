"use strict";
// Access HTML elements
let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let operation = document.getElementById("operation");
let calculate = document.getElementById("start");
let result = document.getElementById("result");

// Add click event listener
calculate.addEventListener("click", function() {

    // Get input values and convert them into numbers
    let number1 = Number(num1.value);
    let number2 = Number(num2.value);

    // Get selected operation
    let operator = operation.value;

    let answer;

    // Perform calculation
    switch (operator) {

        case "add":
            answer = number1 + number2;
            break;

        case "sub":
            answer = number1 - number2;
            break;

        case "multi":
            answer = number1 * number2;
            break;

        case "div":
            if (number2 === 0) {
                result.textContent = "Cannot divide by zero!";
                return;
            }
            answer = number1 / number2;
            break;
    }

    // Display result
    result.textContent = `Result: ${answer}`;
});