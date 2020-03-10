<!DOCTYPE html>
<html>
<body>

<?php
$direction = $_GET['direction'];

$con = mysqli_connect('localhost','phpmyadmin','root','pi');
if (!$con) {
  die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"pi");

$sql = "UPDATE carMotorData SET direction='".$direction."' WHERE id='1'";

$result = mysqli_query($con,$sql);
//echo $direction;
mysqli_close($con);
?>
</body>
</html>

