# 4 Servo can be controlled using this script
# This script will fetch degree value of servo motor from MySQL database
# By updating the degree value in database we can control Servo motor
# Database table will be like:
#      servoData        //Table Name
# | ServoNo | Degree |
# |    1    |   90   |
# |    2    |   80   |
# |    3    |   36   |
# |    4    |   87   |

import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
from time import sleep

#Servo pin define
servoPin1=11    # GPIO 17
servoPin2=12    # GPIO 18
servoPin3=13    # GPIO 27
servoPin4=15    # GPIO 22

# Delay of servo
ServoDelay = 0.2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin1,GPIO.OUT)
GPIO.setup(servoPin2,GPIO.OUT)
GPIO.setup(servoPin3,GPIO.OUT)
GPIO.setup(servoPin4,GPIO.OUT)

pwm1=GPIO.PWM(servoPin1,50)
pwm2=GPIO.PWM(servoPin2,50)
pwm3=GPIO.PWM(servoPin3,50)
pwm4=GPIO.PWM(servoPin4,50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

def SetAngle(angle,ServoNo):
    duty=angle/18+2
    if(ServoNo==1):
        GPIO.output(servoPin1,True)
        pwm1.ChangeDutyCycle(duty)
        sleep(ServoDelay)
        GPIO.output(servoPin1,False)
        pwm1.ChangeDutyCycle(0)
    elif(ServoNo==2):
        GPIO.output(servoPin2,True)
        pwm2.ChangeDutyCycle(duty)
        sleep(ServoDelay)
        GPIO.output(servoPin2,False)
        pwm2.ChangeDutyCycle(0)
    elif(ServoNo==3):
        GPIO.output(servoPin3,True)
        pwm3.ChangeDutyCycle(duty)
        sleep(ServoDelay)
        GPIO.output(servoPin3,False)
        pwm3.ChangeDutyCycle(0)
    elif(ServoNo==4):
        GPIO.output(servoPin4,True)
        pwm4.ChangeDutyCycle(duty)
        sleep(ServoDelay)
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
    GPIO.cleanup()
    print("Ctl C pressed - ending program")
    
