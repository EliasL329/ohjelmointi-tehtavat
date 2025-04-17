async function chuckNorris(query) {
    try {
        const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${query}`);
        const joke = await response.json();
        return (joke.result[0].value);
    } catch (error) {
        console.log(error.message);
    };
};

const form = document.querySelector('form');
form.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const search = document.querySelector('input[name=q]');
    const joke = await chuckNorris(search.value);
    const article = document.createElement('article');
    
    const p = document.createElement('p');
    p.innerText = joke;
    article.appendChild(p);
    
    const results = document.querySelector('#results');
    results.innerHTML = '';
    results.appendChild(article);
});