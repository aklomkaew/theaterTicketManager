$(document).ready(() => {
  function getSeatIndex(seat_id) {
    var c = ''
    for(i = seat_id.length - 1; i >= 0; i--) {
      c = seat_id[i];
      if(c >= '0' && c <= '9') {

      }
      else {
        return i + 1;
      }
    }
  }
  function getSeatListItemSeason(seat_id) {
    var rowIndex = getSeatIndex(seat_id);
    var row_str = seat_id.substring(0,rowIndex);
    var seat_no_str = seat_id.substring(rowIndex);
    var day_str = parent.day.charAt(0).toUpperCase() + parent.day.slice(1)
    var seatListItem = '<li id="ticket-' + parent.nextTicket + '" ';
    seatListItem += 'class="list-group-item d-flex justify-content-between lh-condensed"><div><h6 class="my-0">';
    seatListItem += 'Season Ticket: ' + parent.showName + " " +'Row ' + row_str + ' Seat ' + seat_no_str;
    seatListItem += '</h6><small class="text-muted">';
    seatListItem += ' '  + day_str + " - " + parent.hour + ":" + parent.minute + " " + parent.am_pm_string;
    seatListItem += '</small><span><small class="text-muted">';
    seatListItem += ' ' + parent.theaterName + ' ';
    seatListItem += '</small></span></div><span class="text-muted"></span></li>';
    return seatListItem;
  }

  function getSeatListItem(seat_id) {
    if (parent.isSeason) {
      return getSeatListItemSeason(seat_id);
    }
    else {
      var rowIndex = getSeatIndex(seat_id);
      var row_str = seat_id.substring(0,rowIndex);
      var seat_no_str = seat_id.substring(rowIndex);
      console.log(parent.nextTicket);
      var seatListItem = '<li id="ticket-' + parent.nextTicket + '" ';
      seatListItem += 'class="list-group-item d-flex justify-content-between lh-condensed"><div><h6 class="my-0">';
      seatListItem += 'Row ' + row_str + ' Seat ' + seat_no_str;
      seatListItem += '</h6><small class="text-muted">';
      seatListItem += parent.showName + ' ' + parent.monthName + "/" + parent.day + "/" + parent.year + " - " + parent.hour + ":" + parent.minute + " " + parent.am_pm_string;
      seatListItem += '</small><span><small class="text-muted">';
      seatListItem += ' ' + parent.theaterName + ' ';
      seatListItem += '</small></span></div><span class="text-muted"></span></li>';
      return seatListItem;
    }
  }
  function getNextSelectedSpace(num) {
    var selectedSpace = '<li id="select' + num + '"';
    selectedSpace +=' class="list-group-item d-flex justify-content-between bg-light"><div class="text-success"><h6 class="my-0">Select Seat</h6></div></li>';
    return selectedSpace;
  }
  var nextSelectedSpaceToReplace = 1;
  $('.seat').on('click', function (e) {
      var this_id = $(this).attr('id');
      var numberToSelect = window.parent.$("#seat-spinner").val();
      // var please_work = $('#seat-spinner', window.parent.document).val();
      console.log('Seat clicked!');
      if ($(this).hasClass('available') && parent.numSelected < numberToSelect) {
        $(e.currentTarget).css("background-color", "lime");
        parent.selectedSeats.push(this_id);
        $(this).removeClass('available');
        parent.numSelected += 1;
        // var list_item = '<li class="list-group-item d-flex justify-content-between lh-condensed"><div><h6 class="my-0">Row A Seat 1</h6><small class="text-muted">Scotty McCreedy Oct 30, 2018 - 05:30PM</small><span><small class="text-muted">Concert Hall</small></span></div><span class="text-muted">$10.95</span></li>';
        var list_item = getSeatListItem(this_id);
        // // window.parent.$("#seat-list").append(list_item);
        // window.parent.$(".select-seat").before(list_item);
        var idOfNextSelectToReplace = "#select" + nextSelectedSpaceToReplace;
        console.log()
        window.parent.$(idOfNextSelectToReplace).replaceWith(list_item);
        // window.parent.$('#seat-list li:last-child').remove();
        nextSelectedSpaceToReplace += 1;
        parent.nextTicket += 1;
        console.log(parent.nextTicket);
      }
      else if (parent.selectedSeats.includes(this_id)) {
        console.log('else entered');
        $(e.currentTarget).css("background-color", "grey");
        var index = parent.selectedSeats.indexOf(this_id);
        if (index > -1) {
          parent.selectedSeats.splice(index, 1);
        }
        $(this).addClass('available');
        parent.numSelected -= 1;
        // remove nextTicket from list
        var list_removeID = parent.nextTicket - 1;
        console.log('this: ' + list_removeID);
        // window.parent.$("#ticket-" + list_removeID).remove();
        // decement nextTicket
        parent.nextTicket -= 1;
        var list_item = getNextSelectedSpace(parent.nextSelectedSpaceToCreate);
        window.parent.$("#ticket-" + list_removeID).replaceWith(list_item);
        parent.nextSelectedSpaceToCreate += 1;
      }
});
// $('.no-seat').click(function (e) {
//     $(e.currentTarget).hide();
//     $(document.elementFromPoint(e.clientX, e.clientY)).trigger("click");
//     $(e.currentTarget).show();
// });
$('.handicap-seat').on('click', function (e) {
    var this_id = $(this).attr('id');
    var numberToSelect = window.parent.$("#seat-spinner").val();
    // var please_work = $('#seat-spinner', window.parent.document).val();
    console.log('Handicap Seat clicked!');
    if ($(this).hasClass('handicap-available') && parent.numSelected < numberToSelect) {
      // $(e.currentTarget).css("background-color", "lime");
      $(e.currentTarget).attr('src',"/static/img/handicap-green.png");
      parent.selectedSeats.push(this_id);
      $(this).removeClass('handicap-available');
      parent.numSelected += 1;
      // var list_item = '<li class="list-group-item d-flex justify-content-between lh-condensed"><div><h6 class="my-0">Row A Seat 1</h6><small class="text-muted">Scotty McCreedy Oct 30, 2018 - 05:30PM</small><span><small class="text-muted">Concert Hall</small></span></div><span class="text-muted">$10.95</span></li>';
      var list_item = getSeatListItem(this_id);
      // // window.parent.$("#seat-list").append(list_item);
      // window.parent.$(".select-seat").before(list_item);
      var idOfNextSelectToReplace = "#select" + nextSelectedSpaceToReplace;
      console.log()
      window.parent.$(idOfNextSelectToReplace).replaceWith(list_item);
      // window.parent.$('#seat-list li:last-child').remove();
      nextSelectedSpaceToReplace += 1;
      parent.nextTicket += 1;
      console.log(parent.nextTicket);
    }
    else if (parent.selectedSeats.includes(this_id)) {
      console.log('else entered');
      $(e.currentTarget).attr('src',"/static/img/handicap_logo.png");
      var index = parent.selectedSeats.indexOf(this_id);
      if (index > -1) {
        parent.selectedSeats.splice(index, 1);
      }
      $(this).addClass('handicap-available');
      parent.numSelected -= 1;
      // remove nextTicket from list
      var list_removeID = parent.nextTicket - 1;
      console.log('this: ' + list_removeID);
      // window.parent.$("#ticket-" + list_removeID).remove();
      // decement nextTicket
      parent.nextTicket -= 1;
      var list_item = getNextSelectedSpace(parent.nextSelectedSpaceToCreate);
      window.parent.$("#ticket-" + list_removeID).replaceWith(list_item);
      parent.nextSelectedSpaceToCreate += 1;
    }
        // }
      // var num = window.parent.$("#seat-spinner").val();
      // console.log(window.parent.$("#seat-spinner").val());
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
