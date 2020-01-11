<!DOCTYPE html>
<html>
<body>

<?php
$degree = intval($_GET['degree']);
$servoNo= intval($_GET['servoNo']);

$con = mysqli_connect('localhost','phpmyadmin','root','pi');
if (!$con) {
  die('Could not connect: ' . mysqli_error($con));
}

mysqli_select_db($con,"pi");

$sql = "UPDATE servoData SET degree='".$degree."' WHERE servo_no='".$servoNo."'";

$result = mysqli_query($con,$sql);

echo $degree."(Updated!)";
mysqli_close($con);
?>
</body>
</html>
