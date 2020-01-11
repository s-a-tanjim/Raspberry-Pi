import mysql.connector
from mysql.connector import Error
import RPi.GPIO as GPIO
from time import sleep

#Servo define
servoPin=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin,GPIO.OUT)

pwm=GPIO.PWM(servoPin,50)
pwm.start(0)

def SetAngle(angle):
    duty=angle/18+2
    GPIO.output(servoPin,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPin,False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='pi',
                                         user='phpmyadmin',
                                         password='root')

            sql_select_Query = "select * from servoData where servo_no=1"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            print("\nPrinting servo data")
            for row in records:
                print("Servo No = ", row[0], )
                print("Degree = ", row[1])
                SetAngle(int(row[1]))
                sleep(0.5)

        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    sleep(2)
    print("Ctl C pressed - ending program")
