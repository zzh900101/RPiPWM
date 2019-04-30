import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 17
GPIO_ECHO = 27
led_pin = 4

GPIO.setwarnings(False)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)

p = GPIO.PWM(led_pin,100)
p.start(0)

def distance():
        #set trigger to high
        GPIO.output(GPIO_TRIGGER,True)
        
        #set trigger to low after 0.01ms
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER,False)
        
        StartTime = time.time()
        StopTime = time.time()
        
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
        
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
            
        TimeElaplsed = StopTime - StartTime
        distance = (TimeElaplsed *34300)/2
        
        if (distance > 10):
            distance =10
        elif (distance <0):
            distance =0
            
        return distance
    
try:
    while 1:
        dist = distance()

        print(dist)
        p.ChangeDutyCycle(100-(dist)*10)
        
        time.sleep(0.2)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()