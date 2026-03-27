from gpiozero import PWMOutputDevice, DigitalOutputDevice
import time
import glob
from time import sleep

ENA = PWMOutputDevice(18)
IN1 = DigitalOutputDevice(23)
IN2 = DigitalOutputDevice(24)

ENB = PWMOutputDevice(13)
IN3 = DigitalOutputDevice(27)
IN4 = DigitalOutputDevice(22)

# start pumps
ENA.value = 0.1
ENB.value = 0.1

IN1.on()
IN2.off()

IN3.on()
IN4.off()

TARGET_TEMP = 32

base_dir = '/sys/bus/w1/devices/'
devices = glob.glob(base_dir + '28*')

if not devices:
    raise RuntimeError("No DS18B20 sensor found!")

device_folder = devices[0]

device_file = device_folder + '/w1_slave'

def read_temp():
    with open(device_file, 'r') as f:
        lines = f.readlines()

    # Optional safety check (VERY useful)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        with open(device_file, 'r') as f:
            lines = f.readlines()

    temp_line = lines[1]
    temp_string = temp_line.split('t=')[1]
    temp_c = float(temp_string) / 1000.0

    return temp_c

try:
    while True:
        temp = read_temp()
        print("Temp:", temp)

        hot_speed = 70
        cold_speed = 70

        print("Hot Speed:", hot_speed, "Cold Speed:", cold_speed)

        if temp < TARGET_TEMP:
            cold_speed = 30
            hot_speed = 80

            print("Too low temp Speed:", hot_speed, "Cold Speed:", cold_speed)

        elif temp > TARGET_TEMP:
            hot_speed = 30
            cold_speed = 80

            print("Too high temp Speed:", hot_speed, "Cold Speed:", cold_speed)

        ENA.value = hot_speed / 100
        ENB.value = cold_speed / 100

        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()