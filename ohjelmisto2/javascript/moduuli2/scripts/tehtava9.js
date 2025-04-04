function even(list) {
    const newList = [];

    for (let i of list) {
        if (i % 2 === 0) {
            newList.push(i);
        }
    }
    
    console.log(list);
    console.log(newList);
}

const list = [1, 2, 3, 4, 5, 6];
even(list);