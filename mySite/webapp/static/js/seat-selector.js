$(document).ready(() => {
  var str = '';
  $('.seat').on('click', function (e) {
      window.selectedSeats = 'a';
      console.log('Seat clicked');
      console.log(window.selectedSeats);
      $(e.currentTarget).css("background-color", "yellow");
      str += e.target.id;
      str += $(this).attr('id');
});

  $("#button").on('click', () => {
      var link_str = '/confirmationPage/';
      link_str += str;
      window.location = link_str;
  });
});
