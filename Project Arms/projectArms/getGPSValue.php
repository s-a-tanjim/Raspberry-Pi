<?php
$server_name = "localhost";
$server_password = "root";
$server_username = "phpmyadmin";
$db_name = "pi";
$conn = mysqli_connect ( $server_name , $server_username , $server_password , $db_name );

if( $conn->connect_error ){
  die("Connection Failed(server)!");
}

$sql = "SELECT * FROM gps_reading";

if ($data = mysqli_query($conn, $sql)) {
  //success
  $record = mysqli_fetch_array($data);
} else {
  die("Connection Failed!(data retrieve)");
}
?>

<!DOCTYPE html>
<html>
<head>
<title>GPS Value test</title>
</head>
<style>
body{
  font-size:20px;
}
table,tr,td,th{
  border:1px #111 solid;
}
td,th{
  min-width:180px;
}
table{
  margin:10px auto;
}
table caption{
  font-size:25px;
}
.gpstable{
  text-align:center;
}
</style>
<body>

<div class="gpstable">
<table>
  <tr><th>Latitude</th><td><?php echo $record["lat"]; ?></td></tr>
  <tr><th>North/South</th><td><?php echo $record["n_s"]; ?></td></tr>
  <tr><th>Longitude</th><td><?php echo $record["lon"]; ?></td></tr>
  <tr><th>East/West</th><td><?php echo $record["e_w"]; ?></td></tr>
  <tr><th>Time</th><td><?php echo $record["time"]; ?></td></tr>
</table>
<p>*Last updated at <?php echo date("h:i:sa"); ?> (server time)</p>
</div>

</body>
</html>

