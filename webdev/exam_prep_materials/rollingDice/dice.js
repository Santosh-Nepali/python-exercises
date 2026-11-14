"use strict";

const dice = document.querySelector("#dice");
const rollBtn = document.querySelector("#rollBtn");
const result = document.querySelector("#result");

const diceFaces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"];

rollBtn.addEventListener("click", function () {

    rollBtn.disabled = true;
    result.textContent = "Rolling...";

    let counter = 0;

    const animation = setInterval(function () {

        let randomNumber = Math.floor(Math.random() * 6);

        dice.textContent = diceFaces[randomNumber];

        counter++;

        if (counter === 15) {

            clearInterval(animation);

            result.textContent = "You rolled: " + (randomNumber + 1);

            rollBtn.disabled = false;
        }

    }, 100);

    dice.classList.add("rolling");

    setTimeout(function () {
        dice.classList.remove("rolling");
    }, 500);

});