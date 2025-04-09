const button = document.querySelector('#start');

button.addEventListener('click', function(event) {
    const input = document.querySelector('#calculation').value.toString();
    const values = input.split(/\D/);
    let calculation = 0;

    if (input.includes('+')) {
        calculation = Number(values[0]) + Number(values[1]);
    }
    else if (input.includes('-')) {
        calculation = Number(values[0]) - Number(values[1]);
    }
    else if (input.includes('*')) {
        calculation = Number(values[0]) * Number(values[1]);
    }
    else {
        calculation = Number(values[0]) / Number(values[1]);
    };
    
    document.querySelector('#result').innerHTML = calculation;
});
