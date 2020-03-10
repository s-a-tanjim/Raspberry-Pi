# About
This project is to control mechanical arm(using servo), and control a car (using gps data from gps sensor).

### File Structure
### ServerSide (Those file will be displayed on browser) File location: '/var/www/html/ServerSide/'
 - index.html -> This is the landing page This file location will be: '/var/www/html/index.html'
 - main.html -> Other pages are linked here using iframe
 - getGPSValue.php -> This will collect gps data from server
 - ServoControl.html -> Servo degree will be displayed here, and can be updated from here.
 - carControl.html -> Car control dashboard
 - updataServoValueServer.php -> update servo data to server (data will be received from ServoControl.html)
 - updateCarValueServer.php -> Update car direction
### Scripts (Need to run those using terminal)
 - CameraLiveStream.py -> capture img data and direct broadcast to http://pi.local:8000/index.html
 - ServoControl.py -> get data from database and control Servo using PWM
 - carControl.py -> get data from database and control car direction
 - carAndArmControl.py -> Car and Arm both can be control using this.
 - servoControllWithDB.py -> Test script

# Working Process
1. To connect pi with Putty
	  Pi user: pi        (in my case)
	  Pi Password: pi    (in my case)
2. Start NGINX server  (Apache can be used instead of NGINX)
3. pi.local( or ip address of pi) 
	  here u will get 
	    - PHP Myadmin Link (Username: phpmyadmin ,Pw:root)
	    - Project Arm Landing Page
4. Camera, Servo Control script location: Desktop/Project Arm
	- Camera -> cameraLiveStream.py
	- Servo Control -> servoControl.py
Commands:
```sh
$ python3 cameraLiveStream.py
$ python3 servoControl.py
```

### NGINX Commands
```sh
$ service nginx status `To view status`
$ service nginx restart  
`OR`
$ service nginx reload
```
