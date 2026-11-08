
"use strict";

function checkPrime() {

    let number = parseInt(document.getElementById("number").value);

    let isPrime = true;

    if (number <= 1) {
        isPrime = false;
    }
    else {
        for (let i = 2; i < number; i++) {

            if (number % i == 0) {
                isPrime = false;
                break;
            }
        }
    }

    if (isPrime) {
        document.getElementById("result").innerHTML =
            number + " is a Prime Number.";
    }
    else {
        document.getElementById("result").innerHTML =
            number + " is NOT a Prime Number.";
    }
}