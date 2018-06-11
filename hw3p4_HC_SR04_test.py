#hw3p4_HC_SR04_test.py
#Michael McCann

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

trig = 23
echo = 24

print('I am measuring the distance.')

GPIO.setup(trig,GPIO.OUT) #sets GPIO pin 23 to be output (sends signal)
GPIO.setup(echo,GPIO.IN) #sets GPIO pin 23 to input (echo of signal)

GPIO.output(trig, False) #no signal to start to insure stability
print('Waiting for the sensor.') 
time.sleep(2) #waits 2 seconds because hitting enter shakes my table

GPIO.output(trig, True) #sends signal
time.sleep(0.00001) #10 microseconds
GPIO.output(trig, False) #stops signal after 10 micro-sec

while GPIO.input(echo)==0: #while it doesn't detect the echo of the signal, starts clock
	pulse_start = time.time()
	
while GPIO.input(echo)==1: #when echo is detected, stop clock
	pulse_end = time.time()
	
pulse_duration = (pulse_end - pulse_start) #time it takes for signal to reach destination and back

distance = pulse_duration *17150 #(time sent back multiplied by 2*speed of sound)

distance = round(distance, 2) #rounds number

print ('Distance: ' +str(distance)+'cm')

GPIO.cleanup()
