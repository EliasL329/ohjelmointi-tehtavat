const numbers = [];
let num;

for (;;) {
    num = Number(prompt('Insert number'));
    numbers.push(num);

    if (numbers.includes(num)) {
        numbers.sort((a, b) => a- b);
        break;
    }
}

for (let i of numbers) {
    console.log(i);
}