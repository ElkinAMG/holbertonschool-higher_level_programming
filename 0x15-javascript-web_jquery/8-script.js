const fetched = $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  const films = [];

  data.films.forEach((url, i) => {
    films.push($.getJSON(url, (film) => film.title));
  });

  console.log(films);
});
