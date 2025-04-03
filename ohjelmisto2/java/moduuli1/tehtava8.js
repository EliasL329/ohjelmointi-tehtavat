const yearMin = Number(prompt('Input starting year'));
const yearMax = Number(prompt('Input ending year'));

const list = document.querySelector('#target');

let leapYear;
for (let i = yearMin; i <= yearMax; i += 4) {
    if (year % 400 == 0) {
        leapYear = true
    }

    else if (year % 100 == 0) {
        leapYear = false
    }

    else if (year % 4 == 0) {
        leapYear = true
    }

    else {
        leapYear = false
    }

    if (leapYear) {
        list.innerHTML = <li>i</li>
    }
}