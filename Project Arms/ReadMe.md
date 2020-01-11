# About
This project is to control mechanical arm(using servo), and control a car (using gps data from gps sensor).

### File Structure
1. ServerSide (Those file will be displayed on browser)
 - main.html -> This is the index(landing) page, Other pages are linked here.
 - getGPSValue.php -> This will collect gps data from server
 - ServoControl.html -> Servo degree will be displayed here, and can be updated from here.
 - updataServoValueServer.php -> updata servo data to server (data will be received from ServoControl.html)

2. CameraLiveStream.py -> capture img data and direct broadcast to http://pi.local:8000/index.html
3. ServoControl.py -> get data from server and control Servo using PWM
