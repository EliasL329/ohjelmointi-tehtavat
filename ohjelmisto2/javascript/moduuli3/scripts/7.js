const target = document.querySelector('#target');
const trigger = document.querySelector('#trigger');

function mouseOver() { 
    target.setAttribute('src', 'img/picB.jpg');
};

function mouseOut() {
    target.setAttribute('src', 'img/picA.jpg')
};

trigger.addEventListener('mouseover', mouseOver);
trigger.addEventListener('mouseout', mouseOut);