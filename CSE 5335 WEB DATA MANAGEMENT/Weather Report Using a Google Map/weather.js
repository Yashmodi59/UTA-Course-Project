// 1002086296
// Yash Jitendra Modi

var marker = null; // initialise the marker
var map =''; //map initialisation

function initialize () {
   // initialize the map to given lal lng co-ord  at map to zoom level 8
   map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 32.75, lng: -97.13 }, //lan lng co-ord
      zoom: 8
   });
   // add onclick event listener
   google.maps.event.addListener(map, 'click', function (e) {
      clickHandler(e.latLng.lat(),e.latLng.lng()); //call clickhandler
   });
}

// remove the last overlay marker from the map
function removeMarker() { // 
    if (marker) { //check if present or not
        marker.setMap(null); // Remove the marker from the map
        marker = null; // bsck to null
    }
}

// send ajax request to get the weather report by city name
function sendRequest () {
   var city = document.getElementById("city").value; // Get the city name from the input field

   var xhr = new XMLHttpRequest();
   xhr.open("GET", "proxy.php?q="+city,true);
   xhr.setRequestHeader("Accept","application/json");
   xhr.onreadystatechange = function () {
       if (this.readyState == 4) { // check response state
          var json = JSON.parse(this.responseText);
          var str = JSON.stringify(json,undefined,2);
          var weatherDescription = json.weather[0].description; // get weather from json
          var temperature = (json.main.temp - 273.15).toFixed(2); // Convert temperature to Celsius
          var humidity = json.main.humidity; // grt humidity
          var location = city; // get city
          var longtitude = json.coord.lon; // get lng
          var latiude = json.coord.lat; // get lat

          // Display weather information
          var weatherInfo = `Weather in ${location}: ${weatherDescription}<br>`; // display the weather in location and its description
          weatherInfo += `Temperature: ${temperature}°C<br>`; // show it in the celcius
          weatherInfo += `Humidity: ${humidity}%`; // show humidity

          document.getElementById("output").innerHTML = weatherInfo; // change the innnerHtml of the output tag to weather info tage
          removeMarker(); // call RemoveMarker will initialse to null

          // Add a marker to the map given lat, lng
          addMarker(latiude, longtitude);

         //  document.getElementById("output").innerHTML = "<pre>" + str + "</pre>";
       }
   };
   xhr.send(null);
}

// add marker to the field
function addMarker(latiude, longtitude) {
   marker = new google.maps.Marker({ // add marker to given position
      position: { lat: latiude, lng: longtitude },
      map: map,
   });

   // Center the map on the marker
   map.panTo({ lat: latiude, lng: longtitude }); // center it
}
// clickHandler when they are called
function clickHandler(lat,lng) {
   removeMarker(); // call remove marker
   addMarker(lat,lng); // add marker at given co-ordinated
   console.log(lat,lng); //print it
   getWeartherDataByLatLng(lat,lng); //call get weather using given co-ord
}

// get weather using lat, lng not city name
function getWeartherDataByLatLng (lat,lng) {

   // excempt the querry part above whole thing is same as sendRequest()
   var xhr = new XMLHttpRequest();
   xhr.open("GET", "proxy.php?lat="+lat+"&lon="+lng,true);
   xhr.setRequestHeader("Accept","application/json");
   xhr.onreadystatechange = function () {
       if (this.readyState == 4) {
          var json = JSON.parse(this.responseText);
          var str = JSON.stringify(json,undefined,2);
          var weatherDescription = json.weather[0].description;
          var temperature = (json.main.temp - 273.15).toFixed(2); // Convert temperature to Celsius
          var humidity = json.main.humidity;
          var longtitude = json.coord.lon;
          var latiude = json.coord.lat;

          // Display weather information
          var weatherInfo = `Weather in (${latiude},${longtitude}): ${weatherDescription}<br>`;
          weatherInfo += `Temperature: ${temperature}°C<br>`;
          weatherInfo += `Humidity: ${humidity}%`;

          document.getElementById("output").innerHTML = weatherInfo;
       }
   };
   xhr.send(null);
}