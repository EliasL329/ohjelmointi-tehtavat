const numbers = [];
let num;

do {
    num = Number(prompt('Insert number. "0" will stop the program'));
    numbers.push(num);
} while (num != 0)

numbers.sort((a, b) => b - a);

for (i of numbers) {
    console.log(i);
}