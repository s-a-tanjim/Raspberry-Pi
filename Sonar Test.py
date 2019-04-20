import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

trig=7
echo=12

GPIO.setup(trig,GPIO.OUT)
GPIO.output(trig,0)

GPIO.setup(echo,GPIO.IN)
time.sleep(0.1)

print("\nPress Ctl C to quit \n")

#starting calculaion...
try:
    while True:
        GPIO.output(trig,1)
        time.sleep(0.00001)
        GPIO.output(trig,0)

        while GPIO.input(echo)==0:
            pass
        start=time.time()

        while GPIO.input(echo) == 1:
            pass
        stop=time.time()

        distance = (stop-start)*170*100     #in cm unit

        print(distance)
        time.sleep(1)   #1 second delay

except KeyboardInterrupt:
  print("Ctl C pressed - ending program")

GPIO.cleanup()


#   distance = time * speed /2
#   speed = 340
#   speed / 2 = 170
#   time = stop - start
#   as long as echo don't receive frequency, echo remains high after trig(after trig=1)
