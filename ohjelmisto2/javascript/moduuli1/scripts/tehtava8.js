const yearMin = Number(prompt('Input starting year'));
const yearMax = Number(prompt('Input ending year'));

const list = document.querySelector('#target');

let leapYear;
for (let i = yearMin; i <= yearMax; i += 4) {
    if (i % 400 == 0) {
        leapYear = true
    }

    else if (i % 100 == 0) {
        leapYear = false
    }

    else if (i % 4 == 0) {
        leapYear = true
    }

    else {
        leapYear = false
    }

    if (leapYear) {
        let li = document.createElement('li');
        li.innerHTML = i;
        list.appendChild(li);
    }
}