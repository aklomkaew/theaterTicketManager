$(document).ready(() => {
  var str = '5';
  $('.seat').on('click', () => {
    console.log(str);
    $(event.currentTarget).css("background-color", "yellow");
    str += event.target.id;
    console.log(str);
    // str += $(this).attr('id');
  });

  $("#button").on('click', () => {
      var link_str = '/confirmationPage/';
      link_str += str;
      window.location = link_str;
  });
});
