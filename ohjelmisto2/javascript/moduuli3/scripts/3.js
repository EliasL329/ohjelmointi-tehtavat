'use strict';
const names = ['John', 'Paul', 'Jones'];
const li = document.querySelector('#target');

for (let i of names) {
    const li = document.createElement('li');
    li.innerHTML = i;
    target.appendChild(li);
};