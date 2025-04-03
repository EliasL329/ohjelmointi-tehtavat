const participantAmount = Number(prompt('Insert amount of participants'));
const participants = [];

for (let i = 1; i <= participantAmount; i++) {
    participants.push(prompt('Insert participant name'));
}   

participants.sort;

list = document.querySelector("#target");

for (let i = 1; i <= participantAmount; i++) {
    let listItem = document.createElement('li');
    listItem.innerHTML = participants[i - 1];
    list.appendChild(listItem);
}