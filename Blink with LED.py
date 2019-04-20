import RPi.GPIO as GPIO     # importing GPIO library
import time                 # importing time library for delay
count=0
led1 = 11
led2 = 13
led3 = 15
GPIO.setmode(GPIO.BOARD)     # enable BOARD pin numberings
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
while(1):
    GPIO.output(led1,1)
    GPIO.output(led2,0)
    GPIO.output(led3,1)
    # Send Output 5V to pin 11
    time.sleep(1)                # introduce 1 second time delay before executing next line of code
    count+=1
    print(count)
    GPIO.output(led1,0)
    GPIO.output(led2,1)# Send Output 0V to pin 11
    GPIO.output(led3,0)
    time.sleep(1)                # introduce 1 second time delay



GPIO.cleanup()               # undo 11 pin as output, that means 11th pin would not function--
                             # --unless it is specified as output after this line : GPIO.cleanup()
