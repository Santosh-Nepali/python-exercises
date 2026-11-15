
"use strict";

// Asking for the number of candidates
let numberOfCandidates = Number(prompt("Enter the number of candidates:"));

// Creating an empty array
let candidates = [];

// Asking for candidate names and store them as objects
for (let i = 0; i < numberOfCandidates; i++) {
    let candidateName = prompt(`Name for candidate ${i + 1}`);

    candidates.push({
        name: candidateName,
        votes: 0
    });
}

//Asking for the number of voters
let numberOfVoters = Number(prompt("Enter the number of voters:"));

// Asking each voter to vote
for (let i = 0; i < numberOfVoters; i++) {

    let vote = prompt(`Voter ${i + 1}, enter candidate name:`);

    // Empty input means an empty vote
    if (vote == null || vote.trim() == "") {
        continue;
    }

    // Finding the candidate whose name matches the vote
    let selectedCandidate = candidates.find(candidate =>
        candidate.name.toLowerCase() == vote.trim().toLowerCase()
    );

    // Increasing the vote count if candidate exists
    if (selectedCandidate) {
        selectedCandidate.votes++;
    } else {
        console.log(`Invalid candidate name: ${vote}`);
    }
}

// Sorting candidates by votes (highest first)
candidates.sort((a, b) => b.votes - a.votes);

// Displaying the winner
if (candidates.length > 0) {
    console.log(
        `The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
    document.querySelector("#resultVoting").innerHTML+=`The Winner is ${candidates[0].name} with ${candidates[0].votes} votes.`;
}

//Display all results
console.log("results:");
document.querySelector("#resultVoting").innerHTML+=`<br>Results:`;

for (let candidate of candidates) {
    console.log(`${candidate.name}: ${candidate.votes} votes`);
    document.querySelector("#resultVoting").innerHTML+=`<pre>    ${candidate.name}: ${candidate.votes} votes </pre>`;
}
