import RPi.GPIO as GPIO
import time
import glob

ENA = 18
IN1 = 23
IN2 = 24

ENB = 13
IN3 = 27
IN4 = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)


pwmA = GPIO.PWM(ENA, 1000)
pwmB = GPIO.PWM(ENB, 1000)

pwmA.start(70)
pwmB.start(70)

GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)

TARGET_TEMP = 32

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

import time

try:
    while True:
        temp = read_temp()
        print("Temp:", temp)

        hot_speed = 70
        cold_speed = 70

        if temp < TARGET_TEMP:
            cold_speed = 30
            hot_speed = 80

        elif temp > TARGET_TEMP:
            hot_speed = 30
            cold_speed = 80

        pwmA.ChangeDutyCycle(hot_speed)
        pwmB.ChangeDutyCycle(cold_speed)

        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()