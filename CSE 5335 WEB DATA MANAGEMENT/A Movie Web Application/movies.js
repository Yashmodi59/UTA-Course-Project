// student Id:- 1002086296
// Name:- Yash Modi

function initialize () {
}

function sendRequest () {
   var xhr = new XMLHttpRequest();
   var query = encodeURI(document.getElementById("form-input").value);
   xhr.open("GET", "proxy.php?method=/3/search/movie&query=" + query);
   xhr.setRequestHeader("Accept","application/json");
   xhr.onreadystatechange = function () {
       if (xhr.readyState == 4) {
          var json = JSON.parse(xhr.responseText);

          tabularInfo = getLeftSectionData(json);
          if (json["results"].length == 0) return callNoDataFound();
         //  var tbody = document.createElement("tbody");
         //  tbody.append(tabularInfo);
         //  console.log(tbody);
         //  document.getElementById("output").innerHTML = "";
          document.getElementById("output").innerHTML.append(tabularInfo);

         //  document.getElementById("output").innerHTML = json + "<pre>" + str + "</pre>";
       }
   };
   xhr.send(null);
}

function getImage(poster_path){
   var elem = document.createElement("img");
   full_path = "http://image.tmdb.org/t/p/w185" + poster_path;
   elem.setAttribute("src", full_path);
   // elem.setAttribute("height", "250px");
   // elem.setAttribute("width", "50%");
   elem.setAttribute("alt", "Image Data of Movie"); 
   elem.style.display = "block"; // Make the image a block element
   elem.style.margin = "0 auto"; // Center justify the image horizontally
   return elem;
}
function getTitle(params) {
   var h2Element = document.createElement("h2");
   h2Element.textContent = "Title:- "+params;
   h2Element.style.textAlign = "center";
   h2Element.style.fontWeight = "bold";
   return h2Element;
}
function getSummary(params) {
   var pElement = document.createElement("p");
   pElement.textContent = params;
   pElement.style.textAlign = "center";
   pElement.style.fontWeight = "italics";
   return pElement;
}
 function getGenres(params) {
   var pElement = document.createElement("p");
   genres='';
   for (let index = 0; index < params.length-1; index++) {
      console.log(params[index]["name"]);
      genres += params[index]["name"] +',';
   }
   genres += params[params.length-1]["name"];
   pElement.textContent = "Genres:-"+genres;
   pElement.style.textAlign = "center";
   return pElement;
 }
 function getCast(params) {
   var pElement = document.createElement("p");
   var boldElement = document.createElement("b");
   var brElement = document.createElement("br");
   boldElement.textContent = "Top 5 Cast:-";
   boldElement.style.textAlign = "center";

   casts='';
   for (let index = 0; index < 4; index++) {
      // console.log(params[index]["name"]);
      casts += params[index]["name"] +',' +' ';
   }
   casts += params[4]["name"];
   var text1 = document.createTextNode(casts);
   pElement.appendChild(boldElement);
   pElement.append(brElement);
   pElement.appendChild(text1);
   return pElement;
 }


function getClickedTopFiveCastData(movieID) {
   console.log(movieID);
   var xhr = new XMLHttpRequest();
   // xhr.open("GET", "proxy.php?method=/3/movie/" + movieID);
   xhr.open("GET", "proxy.php?method=/3/movie/" + movieID + "/credits");
   xhr.setRequestHeader("Accept","application/json");
   xhr.onreadystatechange = function () {
       if (this.readyState == 4) {   
          var json = JSON.parse(this.responseText);
         //  imgInfoContent =	"<img src=\"http://image.tmdb.org/t/p/w185/" + json["poster_path"] + "\">"
         //  document.getElementById("image").innerHTML = imgInfoContent;
         var castElement = getCast(json['cast']); // Get the image element
         document.getElementById("cast").innerHTML = ''; // Clear the existing content
         document.getElementById("cast").appendChild(castElement); // Append the image element to the DOM
        //  document.getElementById("output").innerHTML = json + "<pre>" + str + "</pre>";
       }
   };
   xhr.send(null);  
}

function getClickedMovieData (movieId) {
   console.log(movieId);
   var xhr = new XMLHttpRequest();
   // xhr.open("GET", "proxy.php?method=/3/movie/" + movieID);
   xhr.open("GET", "proxy.php?method=/3/movie/" + movieId);
   xhr.setRequestHeader("Accept","application/json");
   xhr.onreadystatechange = function () {
       if (this.readyState == 4) {   
          var json = JSON.parse(this.responseText);
         //  imgInfoContent =	"<img src=\"http://image.tmdb.org/t/p/w185/" + json["poster_path"] + "\">"
         //  document.getElementById("image").innerHTML = imgInfoContent;
         var imageElement = getImage(json['poster_path']); // Get the image element
         document.getElementById("image").innerHTML = ''; // Clear the existing content
         document.getElementById("image").appendChild(imageElement); // Append the image element to the DOM
        //  document.getElementById("output").innerHTML = json + "<pre>" + str + "</pre>";
       }
   };
   xhr.send(null);
}
function getClickedTitleData (movieId) {
   console.log(movieId);
   var xhr = new XMLHttpRequest();
   // xhr.open("GET", "proxy.php?method=/3/movie/" + movieID);
   xhr.open("GET", "proxy.php?method=/3/movie/" + movieId);
   xhr.setRequestHeader("Accept","application/json");
   xhr.onreadystatechange = function () {
       if (this.readyState == 4) {   
          var json = JSON.parse(this.responseText);
         //  imgInfoContent =	"<img src=\"http://image.tmdb.org/t/p/w185/" + json["poster_path"] + "\">"
         //  document.getElementById("image").innerHTML = imgInfoContent;
         var h2Element = getTitle(json['title']); // Get the image element
         document.getElementById("title").innerHTML = ''; // Clear the existing content
         document.getElementById("title").appendChild(h2Element); // Append the image element to the DOM
        //  document.getElementById("output").innerHTML = json + "<pre>" + str + "</pre>";
       }
   };
   xhr.send(null);
}
function getClickedGenreData (movieId) {
   console.log(movieId);
   var xhr = new XMLHttpRequest();
   // xhr.open("GET", "proxy.php?method=/3/movie/" + movieID);
   xhr.open("GET", "proxy.php?method=/3/movie/" + movieId);
   xhr.setRequestHeader("Accept","application/json");
   xhr.onreadystatechange = function () {
       if (this.readyState == 4) {   
          var json = JSON.parse(this.responseText);
         //  imgInfoContent =	"<img src=\"http://image.tmdb.org/t/p/w185/" + json["poster_path"] + "\">"
         //  document.getElementById("image").innerHTML = imgInfoContent;
         var genresElement = getGenres(json['genres']); // Get the image element
         document.getElementById("genres").innerHTML = ''; // Clear the existing content
         document.getElementById("genres").appendChild(genresElement); // Append the image element to the DOM
        //  document.getElementById("output").innerHTML = json + "<pre>" + str + "</pre>";
       }
   };
   xhr.send(null);
}
function getClickedSummaryData (movieId) {
   console.log(movieId);
   var xhr = new XMLHttpRequest();
   // xhr.open("GET", "proxy.php?method=/3/movie/" + movieID);
   xhr.open("GET", "proxy.php?method=/3/movie/" + movieId);
   xhr.setRequestHeader("Accept","application/json");
   xhr.onreadystatechange = function () {
       if (this.readyState == 4) {   
          var json = JSON.parse(this.responseText);
         //  imgInfoContent =	"<img src=\"http://image.tmdb.org/t/p/w185/" + json["poster_path"] + "\">"
         //  document.getElementById("image").innerHTML = imgInfoContent;
         var summaryElement = getSummary(json['overview']); // Get the image element
         document.getElementById("summary").innerHTML = ''; // Clear the existing content
         document.getElementById("summary").appendChild(summaryElement); // Append the image element to the DOM
        //  document.getElementById("output").innerHTML = json + "<pre>" + str + "</pre>";
       }
   };
   xhr.send(null);
}
function callNoDataFound(){
   alert('No result Found');
}
function onRowClick(id) {
   getClickedMovieData(id);
   getClickedTitleData(id);
   getClickedSummaryData(id);
   getClickedGenreData(id);
   getClickedTopFiveCastData(id);
   // alert('Clicked on row with ID: ' + id);
}

function getLeftSectionData(json){
   const tableBody = document.querySelector('#data-table tbody');

   all_results = json["results"]

   tableBody.innerHTML = '';

   // Use map to create table rows and cells
   const rows = all_results.map(function (item) {
       const row = document.createElement('tr');
       const cell1 = document.createElement('td');
       const cell2 = document.createElement('td');
       const cell3 = document.createElement('td');

       cell1.textContent = item['id'];
       cell2.textContent = item['title'];
       cell3.textContent = item['release_date'].split("-")[0];

       row.appendChild(cell1);
       row.appendChild(cell2);
       row.appendChild(cell3);
       row.onclick = function(){
         onRowClick(item['id']);
       };
       return row;
   });

   // Append the rows to the table body
   rows.forEach(function (row) {
       tableBody.appendChild(row);
   });

   return tableBody;
}
