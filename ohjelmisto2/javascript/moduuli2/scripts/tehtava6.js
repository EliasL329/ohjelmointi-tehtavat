function diceRoll() {
    const result = Math.floor(Math.random() * 6) + 1;
    return result;
}

function main() {
    const list = document.querySelector('#target')
    let dice;

    do {
        let item = document.createElement('li');
        
        dice = diceRoll();
        item.innerHTML = dice

        list.appendChild(item);
    } while (dice < 6);
}

main()