'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const target = document.querySelector('#target')

for (let i = 1; i <= students.length; i++) {
  const option = document.createElement('option');
  option.innerHTML = students[i-1].name;
  option.value = students[i-1].id;
  target.appendChild(option);
};