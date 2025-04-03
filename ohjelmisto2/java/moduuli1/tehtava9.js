const num = Number(prompt('input number'));
let prime = true;

for (let i = 2; i < num; i++) {
    if (num % i == 0) {
        prime = false;
        break;
    }
}

if (prime) {
    document.querySelector('#target').innerHTML = 'is a prime number';
}

else {
    document.querySelector('#target').innerHTML = 'not a prime number';
}