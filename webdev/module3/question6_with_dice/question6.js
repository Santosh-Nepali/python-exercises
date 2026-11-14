"use strict";

const dice = document.querySelector("#dice");
const result = document.querySelector("#result");
const rollBtn = document.querySelector("#rollBtn");

const diceFaces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"];

// Function to generate random dice number
function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

// Main program
rollBtn.addEventListener("click", function () {

    rollBtn.disabled = true;
    result.innerHTML = "";

    let diceNumber;
    let counter = 0;

    const animation = setInterval(function () {

        diceNumber = rollDice();

        dice.textContent = diceFaces[diceNumber - 1];

        dice.classList.remove("rolling");

        // Restart CSS animation
        void dice.offsetWidth;

        dice.classList.add("rolling");

        result.innerHTML += `<li>${diceNumber}</li>`;

        counter++;

        if (diceNumber === 6) {
            clearInterval(animation);
            rollBtn.disabled = false;
        }

    }, 600);

});