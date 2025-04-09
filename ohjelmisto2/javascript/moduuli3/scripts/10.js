const form = document.querySelector('#source');
const fname = document.querySelector('input[name=firstname]');
const lname = document.querySelector('input[name=lastname]');
const p = document.querySelector('#target');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    p.innerHTML = `Your name is ${fname.value} ${lname.value}`;
});