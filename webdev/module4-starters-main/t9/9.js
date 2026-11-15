"use strict";

// Access HTML elements
let calculation = document.getElementById("calculation");
let calculate = document.getElementById("start");
let result = document.getElementById("result");

// Add click event listener
calculate.addEventListener("click", function() {

    // Get the calculation from the input field
    let input = calculation.value;

    let answer;

    // Check which operator is included
    if (input.includes("+")) {

        let numbers = input.split("+");

        let num1 = Number(numbers[0]);
        let num2 = Number(numbers[1]);

        answer = num1 + num2;

    } else if (input.includes("-")) {

        let numbers = input.split("-");

        let num1 = Number(numbers[0]);
        let num2 = Number(numbers[1]);

        answer = num1 - num2;

    } else if (input.includes("*")) {

        let numbers = input.split("*");

        let num1 = Number(numbers[0]);
        let num2 = Number(numbers[1]);

        answer = num1 * num2;

    } else if (input.includes("/")) {

        let numbers = input.split("/");

        let num1 = Number(numbers[0]);
        let num2 = Number(numbers[1]);

        if (num2 === 0) {
            result.textContent = "Cannot divide by zero!";
            return;
        }

        answer = num1 / num2;

    } else {

        result.textContent = "Invalid calculation!";
        return;
    }

    // Display the result
    result.textContent = `Result: ${answer}`;

});