const form = document.querySelector('form');

function createElements(result) {
    for (let i of result) {
        const article = document.createElement('article');
        const name = document.createElement('h2');
        name.innerText = i.show.name;

        const url = document.createElement('a');
        url.innerText = 'Link to details';
        url.href = i.show.url;
        url.target = '_blank';

        const image = document.createElement('img');
        image.src = i.show.image?.medium;
        image.alt = i.show.name;

        const summary = document.createElement('div');
        summary.innerHTML = i.show.summary;

        article.append(name, url, image, summary);
        document.querySelector('#results').appendChild(article);
    };
};

form.addEventListener('submit', async function (evt) {
    evt.preventDefault();
    document.querySelector('#results').innerHTML = '';
    const query = document.querySelector('input[name=q]');
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query.value}`);
        const result = await response.json();
        console.log(result);

        createElements(result);

    } catch (error) {
        console.log(error.message);
    };
});