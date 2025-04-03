const year = Number(prompt('Input year'));
let leapYear;

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
    document.querySelector('#target').innerHTML = 'leap year'
}

else {
    document.querySelector('#target').innerHTML = 'not a leap year'
}