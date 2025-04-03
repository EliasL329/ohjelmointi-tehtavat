const diceAmount = Number(prompt('Insert amount of dice to roll'));
const diceSum = Number(prompt('Insert sum of the eye numbers to calculate'));

let count = 0;
let sum = 0;

for (let i = 1; i <= 10000; i++) {

    for (let i = 1; i <= diceAmount; i++) {
        sum += Math.floor(Math.random() * 6) + 1;
    }
    
    if (sum == diceSum) {
        count += 1;
    }

    sum = 0;
}

const chance = count / 100;

document.querySelector('#target').innerHTML = 'Probability to get sum ' + diceSum + ' with ' + diceAmount + ' dice is ' + chance.toFixed(2) + '%';