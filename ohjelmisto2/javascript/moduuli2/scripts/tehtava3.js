const dogs = [];
const list = document.querySelector('#target');

for (let i = 1; i <= 6; i++) {
    dogs.push(prompt('Insert name of dog'));
}

dogs.sort().reverse();

for (let i = 1; i <= 6; i++) {
    const li = document.createElement('li');
    li.innerHTML = dogs[i - 1];
    list.appendChild(li);
}