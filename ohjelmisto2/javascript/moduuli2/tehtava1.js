const numbers = [];

for (let i = 1; i <= 5; i++) {
    numbers.push(Number(prompt('insert number')))
}

for (let i = 4; i > 0; i--) {
    console.log(numbers[i])
}