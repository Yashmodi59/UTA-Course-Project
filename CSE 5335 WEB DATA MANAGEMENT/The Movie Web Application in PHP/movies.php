<?php
//How to call the MovieDB web services from PHP? Used file_get_contents
// 1002086296
// Yash Jitendra Modi
session_start();
$_SESSION['api_key'] = "b0cf398bca93a1cfbb52c3b57e4e6c69"; // API key is store in the session I know it vulnerable to attack but righ now i am storing to use it everywhere
?>
<!DOCTYPE html>
<html>
<head>
    <title>Movie Search From TMDB</title>
</head>
<body>
<?php
function getRequestedData() {
    // this will handle search result 
    // initial get request request when movie name is search
    // get api key from the session
    // get JSON file from the search result
    // pass it to display result page
    if (isset($_GET['search'])) { // check for search 
        $search = $_GET['search'];// store in var
        $_SESSION['selected_tmdb_id$tmdb_id'] = $search; // store in session
        $f_url = "https://api.themoviedb.org/3/search/movie?api_key={$_SESSION['api_key']}&query=" . urlencode($search); // generate URL
        $data = json_decode(file_get_contents($f_url), true); // generate JSON file
        displaySearchResults($search, $data);// Display result
    } 
}

function displaySearchResults($search, $data) {
    // HTML Code to display result in order list
    if (isset($data['results'])) { // get result from JSON
        echo "<h1>Search Results for \"$search\" obtained form TMDB database</h1>"; 
        echo "<ol>"; // start order list
        // Iterating the first page of result to list movie result
        foreach ($data['results'] as $movie) {
            $release_year = date('Y', strtotime($movie['release_date'])); // get oly year
            echo "<li><a href=\"movies.php?id={$movie['id']}\">{$movie['title']} ({$release_year})</a></li>"; //give URL to get movie data when clicked
        }
        echo "</ol>"; // finish order list
    } else {
        echo "No results found.";
    }
}

function getRequestedMovieData() {
    // get request from the following result data  when they are clicked 
    if (isset($_GET['id'])) {
        $tmdb_id = $_GET['id']; // get ID of the clicked movie data
        $f_url = "https://api.themoviedb.org/3/movie/{$tmdb_id}?api_key={$_SESSION['api_key']}"; // generate URL
        $tmdb_data = json_decode(file_get_contents($f_url), true); // get JSON data
        getEachMovieDetails($tmdb_data); // generate HTML file to display result
    } else {
        echo "Movie not found."; // if no movies of following ID found
    }
}
function getGenreData($tmdb_data) {
    // get the GENRE form JSON file if it is there seperate with COMMA or else print no data found
    if (isset($tmdb_data['genres']) && is_array($tmdb_data['genres']) && count($tmdb_data['genres']) > 0) { //check
        echo "<p><strong>Genres: </strong>" . implode(", ", array_column($tmdb_data['genres'], 'name')) . "</p>"; // seperate with comma
    } else {
        echo "<p><strong>Genres not available for this movie.</strong></p>"; // if not found
    }
}
function getTopFiveCastData($castdata) {
    // get the top 5 cast form JSON file if it is there print in order list or else print no data found
    if (isset($castdata['cast']) && is_array($castdata['cast']) && count($castdata['cast']) > 0) { //check if available
        echo "<p><strong>Top 5 Cast Members: </strong>"; // Get TOp 5 cast
        echo "<ol>"; //start OL
        $cm = array_slice($castdata['cast'], 0, 5); // get top 5 // slice it
        foreach ($cm as $cast) {
            echo "<li>{$cast['name']}</li> ";
        }
        echo "</ol>";
        echo "</p>";
    } else {
        echo "<p><strong>Cast Data not available for this movie.</strong></p>"; // if not found
    }
}
function getEachMovieDetails($tmdb_data) {
    // get movie detail of the clicked movie when it is found
    // get title 
    // get genre detail if available seperated by comma
    // get summary
    // get poster
    // get top 5 cast
    echo "<h1>Title: {$tmdb_data['title']}</h1>"; //title
    echo "<img src=\"https://image.tmdb.org/t/p/w500{$tmdb_data['poster_path']}\" alt=\"Movie Poster\"><br>"; // poster
    getGenreData($tmdb_data); // get genre as required
    echo "<p><strong>Overview: </strong>{$tmdb_data['overview']}</p>"; // get summary
    $curlcast = "https://api.themoviedb.org/3/movie/{$tmdb_data['id']}/credits?api_key={$_SESSION['api_key']}"; 
    $castdata = json_decode(file_get_contents($curlcast), true);
    getTopFiveCastData($castdata); // get top 5 cast
}

// Routing based on the request given in search box
if (isset($_GET['search'])) {
    getRequestedData(); // call to list search result
} elseif (isset($_GET['id'])) {
    getRequestedMovieData();// call to print each movie detail when clicked
} else {// if both blank than display form
    echo "<h1>Movie Search From TMDB database</h1>";
    echo "<form action=\"movies.php\" method=\"get\">"; //get request in PHP form
    echo "<input type=\"text\" name=\"search\" placeholder=\"Enter movie title to search in DB\">"; // get input title
    echo "<input type=\"submit\" value=\"Display Info\">"; // button to submit form
    echo "</form>";
}
session_destroy(); // destroying form
?>
</body>
</html>
