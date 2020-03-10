import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
from time import sleep

#Servo pin define
servoPin1=11
servoPin2=12
servoPin3=13
servoPin4=15

#PWM Value (Speed of motor)
leftPWM1_val=0
leftPWM2_val=0
rightPWM1_val=0
rightPWM2_val=0

#Motor pin define
leftEn1=16
leftEn2=18
leftPWM1_pin=22
leftPWM2_pin=24

rightEn1=29
rightEn2=31
rightPWM1_pin=33
rightPWM2_pin=35

# GPIO Board selection
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin1,GPIO.OUT)
GPIO.setup(servoPin2,GPIO.OUT)
GPIO.setup(servoPin3,GPIO.OUT)
GPIO.setup(servoPin4,GPIO.OUT)
GPIO.setup(leftEn1,GPIO.OUT)
GPIO.setup(leftEn2,GPIO.OUT)
GPIO.setup(leftPWM1_pin,GPIO.OUT)
GPIO.setup(leftPWM2_pin,GPIO.OUT)
GPIO.setup(rightEn1,GPIO.OUT)
GPIO.setup(rightEn2,GPIO.OUT)
GPIO.setup(rightPWM1_pin,GPIO.OUT)
GPIO.setup(rightPWM2_pin,GPIO.OUT)

#Servo PWM set
pwm1=GPIO.PWM(servoPin1,50)
pwm2=GPIO.PWM(servoPin2,50)
pwm3=GPIO.PWM(servoPin3,50)
pwm4=GPIO.PWM(servoPin4,50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

#Motor PWM set
leftPWM1=GPIO.PWM(leftPWM1_pin,50)
leftPWM2=GPIO.PWM(leftPWM2_pin,50)
rightPWM1=GPIO.PWM(rightPWM1_pin,50)
rightPWM2=GPIO.PWM(rightPWM2_pin,50)
leftPWM1.start(0)
leftPWM2.start(0)
rightPWM1.start(0)
rightPWM2.start(0)

#Functions
def go():
    GPIO.output(leftEn1,GPIO.HIGH)
    GPIO.output(leftEn2,GPIO.HIGH)
    leftPWM1.ChangeDutyCycle(leftPWM1_val)
    leftPWM2.ChangeDutyCycle(leftPWM2_val)
    
    GPIO.output(rightEn1,GPIO.HIGH)
    GPIO.output(rightEn2,GPIO.HIGH)
    rightPWM1.ChangeDutyCycle(rightPWM1_val)
    rightPWM2.ChangeDutyCycle(rightPWM2_val)

def forward():
    go()
def backward():
    go()
def left():
    go()
def right():
    go()

def stop():
    GPIO.output(leftEn1,GPIO.LOW)
    GPIO.output(leftEn2,GPIO.LOW)
    leftPWM1.ChangeDutyCycle(0)
    leftPWM2.ChangeDutyCycle(0)
    
    GPIO.output(rightEn1,GPIO.LOW)
    GPIO.output(rightEn2,GPIO.LOW)
    rightPWM1.ChangeDutyCycle(0)
    rightPWM2.ChangeDutyCycle(0)

def driveMotor(direction):
    if(direction=='f'):
        leftPWM1_val=50
        leftPWM2_val=0
        rightPWM1_val=50
        rightPWM2_val=0
        forward()
    elif(direction=='b'):
        leftPWM1_val=0
        leftPWM2_val=50
        rightPWM1_val=0
        rightPWM2_val=50
        backward()
    elif(direction=='l'):
        leftPWM1_val=0
        leftPWM2_val=50
        rightPWM1_val=50
        rightPWM2_val=0
        left()
    elif(direction=='r'):
        leftPWM1_val=50
        leftPWM2_val=0
        rightPWM1_val=0
        rightPWM2_val=50
        right()
    else:
        stop()


def SetAngle(angle,ServoNo):
    duty=angle/18+2
    if(ServoNo==1):
        GPIO.output(servoPin1,True)
        pwm1.ChangeDutyCycle(duty)
        sleep(.3)
        GPIO.output(servoPin1,False)
        pwm1.ChangeDutyCycle(0)
    elif(ServoNo==2):
        GPIO.output(servoPin2,True)
        pwm2.ChangeDutyCycle(duty)
        sleep(.3)
        GPIO.output(servoPin2,False)
        pwm2.ChangeDutyCycle(0)
    elif(ServoNo==3):
        GPIO.output(servoPin3,True)
        pwm3.ChangeDutyCycle(duty)
        sleep(.3)
        GPIO.output(servoPin3,False)
        pwm3.ChangeDutyCycle(0)
    elif(ServoNo==4):
        GPIO.output(servoPin4,True)
        pwm4.ChangeDutyCycle(duty)
        sleep(.3)
        GPIO.output(servoPin4,False)
        pwm4.ChangeDutyCycle(0)

#Main Loop
try:
    while True:
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='pi',
                                         user='phpmyadmin',
                                         password='root')

            sql_select_Query = "select * from servoData"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            print("\nPrinting servo data")
            ServoNo=1
            for row in records:
                print("Servo No= ",row[0],"   |   Degree= ",row[1])
                SetAngle(int(row[1]),ServoNo)
                ServoNo+=1

            sql_select_Query = "select * from carMotorData where id='1'"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            row = cursor.fetchall()

            print("\nPrinting carMotor data")
            print("Direction= ",row[0][1])
            driveMotor(row[0][1])
            sleep(0.02)

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
        
except KeyboardInterrupt:
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()
    leftPWM1.stop()
    leftPWM2.stop()
    rightPWM1.stop()
    rightPWM2.stop()
    GPIO.cleanup()
    print("Ctl C pressed - ending program")

        

