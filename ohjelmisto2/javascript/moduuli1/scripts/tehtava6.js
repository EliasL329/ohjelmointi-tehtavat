const answer = confirm('Should I calculate the square root?');

if (answer) {
    const num = Number(prompt('Input number'));

    if (num >= 0) {
        const sqrRoot = Math.sqrt(num)
        document.querySelector('#target').innerHTML = 'The square root of ' + num + ' is ' + sqrRoot;
    }

    else {
        document.querySelector('#target').innerHTML = 'The square root of a negative number is not defined';
    }
}