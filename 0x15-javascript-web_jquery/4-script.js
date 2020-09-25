$('DIV#toggle_header').click(() => {
  const cls = $('header').attr('class');
  $('header').toggleClass('green red');
});
