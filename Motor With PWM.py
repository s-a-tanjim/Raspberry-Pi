import RPi.GPIO as GPIO
import time

RMP=36   #Right Motor Plus
RMM=38   #Right Motor Minus
RPWM=40  #Right PWM

LMP=33   #Left Motor Plus
LMM=35   #Left Motor Minus
LPWM=37  #Left PWM

PWM=0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(RMP,GPIO.OUT)
GPIO.setup(RMM,GPIO.OUT)
GPIO.setup(RPWM,GPIO.OUT)
GPIO.setup(LMP,GPIO.OUT)
GPIO.setup(LMM,GPIO.OUT)
GPIO.setup(LPWM,GPIO.OUT)

rpwm=GPIO.PWM(RPWM,100)   #100 Hz
lpwm=GPIO.PWM(LPWM,100)   #100 Hz

rpwm.start(PWM)
lpwm.start(PWM)

def forward():
    GPIO.output(RMP,GPIO.HIGH)
    GPIO.output(RMM,GPIO.LOW)
    rpwm.ChangeDutyCycle(PWM)
    
    GPIO.output(LMP,GPIO.HIGH)
    GPIO.output(LMM,GPIO.LOW)
    lpwm.ChangeDutyCycle(PWM)
    
def backward():
    GPIO.output(RMP,GPIO.LOW)
    GPIO.output(RMM,GPIO.HIGH)
    rpwm.ChangeDutyCycle(PWM)
    
    GPIO.output(LMP,GPIO.LOW)
    GPIO.output(LMM,GPIO.HIGH)
    lpwm.ChangeDutyCycle(PWM)
    
def left():
    GPIO.output(RMP,GPIO.HIGH)
    GPIO.output(RMM,GPIO.LOW)
    rpwm.ChangeDutyCycle(PWM)
    
    GPIO.output(LMP,GPIO.LOW)
    GPIO.output(LMM,GPIO.HIGH)
    lpwm.ChangeDutyCycle(PWM)
    
def right():
    GPIO.output(RMP,GPIO.LOW)
    GPIO.output(RMM,GPIO.HIGH)
    rpwm.ChangeDutyCycle(PWM)
    
    GPIO.output(LMP,GPIO.HIGH)
    GPIO.output(LMM,GPIO.LOW)
    lpwm.ChangeDutyCycle(PWM)
    
def stop():
    GPIO.output(RMP,GPIO.LOW)
    GPIO.output(RMM,GPIO.LOW)
    rpwm.ChangeDutyCycle(0)
    
    GPIO.output(LMP,GPIO.LOW)
    GPIO.output(LMM,GPIO.LOW)
    lpwm.ChangeDutyCycle(0)
    

try:
    while True:
        PWM=100
        forward()
        print('Forward')
        time.sleep(5)
        PWM=10
        backward()
        print('Backward')
        time.sleep(5)
        PWM=50
        left()
        print('Left')
        time.sleep(5)
        right()
        print('Right')
        time.sleep(5)
    
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")

rpwm.stop()
lpwm.stop()
GPIO.cleanup()