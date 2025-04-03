const diceRolls = Number(prompt('Input amount of dice rolls'));
let sum = 0;

for (let i = 1; i <= diceRolls; i++) {
    sum += Math.floor(Math.random() * 6) + 1
    console.log(sum)
}

document.querySelector('#target').innerHTML = sum;