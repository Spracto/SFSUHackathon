console.log('hello world');

// require('https://maps.googleapis.com/maps/api/js?key=AIzaSyDNcQPa5xFEY1fUfzEE-lV_Y99mCykigZo&callback=initMap')
function initMap() {
  // Create a map object and specify the DOM element for display.
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.7749, lng: -122.4194},
    scrollwheel: false,
    zoom: 12
  });

}
// function initMapAddress(address) {
//   // Create a map object and specify the DOM element for display.
//   var map = new google.maps.Map(document.getElementById('mapAddress'), {
//     center: {lat: 37.7749, lng: -122.4194},
//     scrollwheel: false,
//     zoom: 12
//   });
//
// }
