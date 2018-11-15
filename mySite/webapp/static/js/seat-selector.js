$(document).ready(() => {
  var str = '';
  // $('.seat').on('click', () => {
  //   console.log(str);
  //   // $(event.currentTarget).css("background-color", "yellow");
  //   str += event.target.id;
  //   console.log(str);
  //   // str += $(this).attr('id');
  // });
  $('.seat').on('click', function (e) {
      console.log(str);
      $(e.currentTarget).css("background-color", "yellow");
      str += e.target.id;
      console.log(str);
      str += $(this).attr('id');
});

  $("#button").on('click', () => {
      var link_str = '/confirmationPage/';
      link_str += str;
      window.location = link_str;
  });
});
