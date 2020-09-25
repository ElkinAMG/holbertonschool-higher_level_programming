$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  data.films.forEach((url, i) => {
    $.getJSON(url, (film) => {
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    });
  });
});
