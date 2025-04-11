const form = document.querySelector('form');

form.addEventListener('submit', async function (evt) {
    evt.preventDefault();
    const query = document.querySelector('input[name=q]');
    try {
        const test = await fetch(`https://api.tvmaze.com/search/shows?q=${query.value}`);
        const result = await test.json();
        console.log(result);
    } catch (error) {
        console.log(error.message);
    };
});