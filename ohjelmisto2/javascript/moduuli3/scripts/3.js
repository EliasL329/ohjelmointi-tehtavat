'use strict';
const names = ['John', 'Paul', 'Jones'];
const li = document.querySelector('#target');

for (let i = 1; i <= names.length; i++) {
    const li = document.createElement('li');
    li.innerHTML = names[i-1];
    target.appendChild(li);
}