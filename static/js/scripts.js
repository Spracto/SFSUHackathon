console.log('hello world');
// $.getScript("my_lovely_script.js", function(){
//
//    alert("Script loaded but not necessarily executed.");
//
// });
// require('https://maps.googleapis.com/maps/api/js?key=AIzaSyDNcQPa5xFEY1fUfzEE-lV_Y99mCykigZo&callback=initMap')
function initMap() {
  // Create a map object and specify the DOM element for display.
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    scrollwheel: false,
    zoom: 8
  });
}
