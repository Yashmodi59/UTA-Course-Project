<?php
  // put your API key here:
  $appid = "89a64415ff9355b28133c8d646133db0";

  header("Content-type: application/json\n\n");
  $params = $_SERVER['QUERY_STRING'];
  $host = "https://api.openweathermap.org/data/2.5/weather?$params&APPID=$appid";
  $ch = curl_init($host);
  curl_exec($ch);
  curl_close($ch);
?>
