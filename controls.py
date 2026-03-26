import RPi.GPIO as GPIO


ENA = 18
IN1 = 23
IN2 = 24

ENB = 13
IN3 = 27
IN4 = 22

#numbering code is classic
GPIO.setmode(GPIO.BCM)


GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)