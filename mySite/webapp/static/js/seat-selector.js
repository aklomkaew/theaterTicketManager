$(document).ready(() => {
  $('.seat').on('click', function (e) {
      var this_id = $(this).attr('id');
      console.log('Seat clicked');
      if ($(this).hasClass('available')) {
        $(e.currentTarget).css("background-color", "lime");
        parent.selectedSeats.push(this_id);
        $(this).removeClass('available');

      }
      else if (parent.selectedSeats.includes(this_id)) {
        console.log('else entered');
        $(e.currentTarget).css("background-color", "grey");
        var index = parent.selectedSeats.indexOf(this_id);
        if (index > -1) {
          parent.selectedSeats.splice(index, 1);
        }
        $(this).addClass('available');
      }
      // console.log(parent.selectedSeats);
      // $(e.currentTarget).css("background-color", "yellow");
      // str += e.target.id;
      // str += $(this).attr('id');
});

  $("#button").on('click', () => {
      var link_str = '/confirmationPage/';
      link_str += str;
      window.location = link_str;
  });
});
