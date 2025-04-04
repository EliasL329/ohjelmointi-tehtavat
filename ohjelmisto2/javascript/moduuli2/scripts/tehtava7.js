function diceRoll(sides) {
    const result = Math.floor(Math.random() * sides) + 1;
    return result;
}

function main() {
    const sides = Number(prompt('Insert amount of sides'));
    const list = document.querySelector('#target')
    let dice;

    do {
        let item = document.createElement('li');
        
        dice = diceRoll(sides);
        item.innerHTML = dice;

        list.appendChild(item);
    } while (dice < sides);
}


main();