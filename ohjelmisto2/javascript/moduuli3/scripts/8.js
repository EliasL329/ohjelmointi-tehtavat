const button = document.querySelector('#start');

button.addEventListener('click', function(event){
    const input1 = document.querySelector('#num1').value;
    const input2 = document.querySelector('#num2').value;
    
    let num1 = Number(input1);
    let num2 = Number(input2);

    const operation = document.querySelector('#operation').value;

    switch (operation) {
        case 'add':
            num1 += num2;
            break;
        case 'sub':
            num1 -= num2;
            break;
        case 'multi':
            num1 *= num2;
            break;
        case 'div':
            num1 /= num2;
            break;
        default:
    };  

    const result = document.querySelector('#result');
    result.innerHTML = num1;
});

