import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
from time import sleep

#PWM Value (Speed of motor)
leftPWM1_val=0
leftPWM2_val=0
rightPWM1_val=0
rightPWM2_val=0

#Motor pin define
leftEn1=11
leftEn2=12
leftPWM1_pin=13
leftPWM2_pin=15

rightEn1=29
rightEn2=31
rightPWM1_pin=33
rightPWM2_pin=35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftEn1,GPIO.OUT)
GPIO.setup(leftEn2,GPIO.OUT)
GPIO.setup(leftPWM1_pin,GPIO.OUT)
GPIO.setup(leftPWM2_pin,GPIO.OUT)
GPIO.setup(rightEn1,GPIO.OUT)
GPIO.setup(rightEn2,GPIO.OUT)
GPIO.setup(rightPWM1_pin,GPIO.OUT)
GPIO.setup(rightPWM2_pin,GPIO.OUT)

leftPWM1=GPIO.PWM(leftPWM1_pin,50)
leftPWM2=GPIO.PWM(leftPWM2_pin,50)
rightPWM1=GPIO.PWM(rightPWM1_pin,50)
rightPWM2=GPIO.PWM(rightPWM2_pin,50)

leftPWM1.start(0)
leftPWM2.start(0)
rightPWM1.start(0)
rightPWM2.start(0)

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


#Main Loop
try:
    while True:
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='pi',
                                         user='phpmyadmin',
                                         password='root')

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
    leftPWM1.stop()
    leftPWM2.stop()
    rightPWM1.stop()
    rightPWM2.stop()
    GPIO.cleanup()
    print("Ctl C pressed - ending program")




