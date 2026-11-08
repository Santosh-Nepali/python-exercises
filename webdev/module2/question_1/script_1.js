
"use strict";

function checkPrime() {

    let number1 = parseInt(document.getElementById("number1").value);

    let isPrime = true;

    if (number1 <= 1) {
        isPrime = false;
    }
    else {
        for (let i = 2; i < number1; i++) {

            if (number1 % i == 0) {
                isPrime = false;
                break;
            }
        }
    }

    if (isPrime) {
        document.getElementById("result").innerHTML =
            `${number1}  is a Prime Number.`;
    }
    else {
        document.getElementById("result").innerHTML =
            `${number1}  is NOT a Prime Number.`;
    }
}