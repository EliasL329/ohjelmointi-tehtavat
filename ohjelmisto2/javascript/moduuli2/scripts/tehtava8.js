function concat(list) {
    let string = '';

    for (let i of list) {
        string += i;
    } 

    document.querySelector('#target').innerHTML = string;
}

const list = ['Johnny', 'DeeDee', 'Joey', 'Marky'];

concat(list);