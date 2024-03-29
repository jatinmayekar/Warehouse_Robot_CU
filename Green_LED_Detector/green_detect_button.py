"""
Game: StopIt!
* Its a simple game consisting of five LED lights and one pushbutton switch. 
* The LEDs flash in a sequence and the player must press the button when the Green LED light is lit. 
* The speed at which the lights flash increases until the player presses the button at the wrong time.

"""
import RPi.GPIO as GPIO
import time
#from gd1 import gd2
# Pin Definitons:
#pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
led = [18,20,21,23,25,26,27]
b = 4 # button pin
k = 0  #counter to check if green led goes high or not
dc = 100 # duty cycle (0-100) for PWM pin
c = 0 #counter of button
a = 0
e = 0 #win counter 

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(b,GPIO.OUT)
for i in range(0,7):
    GPIO.setup(led[i], GPIO.OUT) # LED pin set as output




print("Here we go! Press CTRL+C to exit")
try:
    while True:
        #if k == 1:
                #time.sleep(0.5)
        #g = gd2()
        #print("g",g)
        
        for i in range(0,7):
            if GPIO.input(b) == 1:
                c = c+1
            if c >= 2:
                c = 0
            if i == 3:
                pwm = GPIO.PWM(led[i],50)
                pwm.start(100)
                GPIO.output(led[i], GPIO.HIGH)
                if GPIO.input(b) == 1:
                    if c==1:
                        k=1
                        c=0
                        GPIO.output(led[i], GPIO.HIGH)
                        time.sleep(3)
                        GPIO.output(led[i], GPIO.LOW)
                    else:
                       print('please remove your hand')
                       time.sleep(5)
                #time.sleep(0.5)
                GPIO.output(led[i], GPIO.LOW)
                pwm.stop()
            pwm = GPIO.PWM(led[i],50)
            pwm.start(dc)
            GPIO.output(led[i], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led[i], GPIO.LOW)
            pwm.stop()
            print('Button',GPIO.input(b))
            print('Iteration',i)
            print('Counter',c)
            print('win counter',e)
            #if i==3 :
                    #print('WIN!!!')
                    #c = c+1
                    #time.sleep(0.1)
            if k == 1:
                print('win! =',e)
                #time.sleep(3)
                GPIO.output(led[3],GPIO.HIGH)
                time.sleep(2)
                GPIO.output(led[3],GPIO.LOW)
                k = 0
                e = e+1
                GPIO.output(b, GPIO.LOW)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    #pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO
