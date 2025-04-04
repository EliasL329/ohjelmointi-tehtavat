function election() {
    const candidates = [];
    const candidatesAmount = Number(prompt('Insert amount of candidates'));
    let participant;

    for (let i = 1; i <= candidatesAmount; i++) {
        participant = {};
        participant.firstName = prompt('Name for candidate ' + i);
        participant.votes = 0;

        candidates.push(participant);
        console.log(candidates);
    }

    const voters = Number(prompt('Insert amount of voters'));
    for (let i = 1; i <= voters; i++) {
        const vote = prompt('Insert candidate name you are voting for');

        for (let i of candidates) {
            if (i.firstName === vote) {
                i.votes += 1;
            }
        }
    }
}

election();