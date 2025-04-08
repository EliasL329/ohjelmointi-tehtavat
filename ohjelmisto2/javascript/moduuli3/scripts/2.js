const target = document.querySelector('#target');

const pos = ['First', 'Second', 'Third'];

for (let i = 1; i <= 3; i++) {
    const li = document.createElement('li');
    li.innerHTML = pos[i-1] + ' item';
    target.appendChild(li);
}

const secondItem = document.querySelectorAll('li')[1];
secondItem.className = 'my-item';