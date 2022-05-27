import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 24
Motor1B = 23
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)              # GPIO Numbering
GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
GPIO.setup(Motor1B,GPIO.OUT)


p=GPIO.PWM(Motor1A,50)
p1=GPIO.PWM(Motor1B,50)
p.start(0)  
p1.start(0)

while True:
     for i in range(100,-1,-1):
         p1.ChangeDutyCycle(i)
         sleep(0.1)
     GPIO.cleanup()
     break
        
        
    
            
    
   
   
     
        
        

#
