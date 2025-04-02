const userName = prompt('Type a name');
const randomInt = Math.floor(Math.random() * 4) + 1;

let userClass = ''

if (randomInt == 1) {
    userClass = 'Gryffindor'
}

else if (randomInt == 2) {
    userClass = 'Slytherin'
}

else if (randomInt == 3) {
    userClass = 'Hufflepuff'
}

else {
    userClass = 'Ravenclaw'
}

document.querySelector('#target').innerHTML = userName + ', you are ' + userClass;