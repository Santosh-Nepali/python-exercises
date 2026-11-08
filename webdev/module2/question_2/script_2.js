
"use strict";

function calculateProbability() {

    // Get values from HTML input fields
    let numberOfDice = Number(document.getElementById("dice").value);
    let desiredSum = Number(document.getElementById("sum").value);

    // Validate input
    if (!Number.isInteger(numberOfDice) || numberOfDice < 1 ||
        !Number.isInteger(desiredSum)) {

        document.getElementById("result").innerHTML =
            "Please enter valid positive integers.";

        return;
    }

    // Number of simulations
    let totalRolls = 100000;

    // Count successful results
    let successfulRolls = 0;

    // Roll the dice many times
    for (let i = 0; i < totalRolls; i++) {

        let totalSum = 0;

        // Roll each die
        for (let j = 0; j < numberOfDice; j++) {

            let randomNumber = Math.floor(Math.random() * 6) + 1;

            totalSum += randomNumber;
        }

        // Check whether the sum matches
        if (totalSum === desiredSum) {
            successfulRolls++;
        }
    }

    // Calculate probability
    let probability = successfulRolls / totalRolls;

    let percentage = probability * 100;

    // Display result
    document.getElementById("result").innerHTML =`The number of dices : ${numberOfDice} <br> Sum : ${desiredSum} <br>Probability: ${percentage.toFixed(2)}%`;
}
