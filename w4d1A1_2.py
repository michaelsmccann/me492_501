#w4d1A1_2.py
#Michael McCann
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins_in = [23,24]

GPIO.setup(pins_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pin_out = 18

GPIO.setup(pin_out, GPIO.OUT)
pwm_led = GPIO.PWM(18,500)

n=50
pwm_led.start(n)

try:
	while True:
		if GPIO.input(pins_in[0]) == False:
			print('Button 1 Pressed.')
			while (n<=95):
				p=n+5
				pwm_led.ChangeDutyCycle(p)
				n=p
				time.sleep(0.1)
			pwm_led.ChangeDutyCycle(50)

		elif GPIO.input(pins_in[1]) == False:
			print('Button 2 Pressed.')
			while (n>=5):
				w=n-5
				pwm_led.ChangeDutyCycle(w)
				n=w
				time.sleep(0.1)
			pwm_led.ChangeDutyCycle(50)
except KeyboardInterrupt:
	GPIO.cleanup()
