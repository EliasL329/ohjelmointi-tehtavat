const target = document.querySelector('#target');

const pos = ['First', 'Second', 'Third'];

for (let i of pos) {
    const li = document.createElement('li');
    li.innerHTML = i + ' item';
    target.appendChild(li);
};

const secondItem = document.querySelectorAll('li')[1];
secondItem.className = 'my-item';