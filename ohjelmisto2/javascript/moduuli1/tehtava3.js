const num1 = Number(prompt('1. Number'));
const num2 = Number(prompt('2. Number'));
const num3 = Number(prompt('3. Number'));

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;


document.querySelector('#target').innerHTML = 'Sum: ' + sum + ' Product: ' + product + ' Average:' + average;