# Untitled - By: Alex Soto - jue. feb. 8 2024

from fpioa_manager import fm
from Maix import GPIO
import time

io_led_1 = 12
io_led_red = 13
io_led_3 = 14

fm.register(io_led_1, fm.fpioa.GPIO0)
fm.register(io_led_red, fm.fpioa.GPIO1)
fm.register(io_led_3, fm.fpioa.GPIO2)

led_1=GPIO(GPIO.GPIO0, GPIO.OUT)
led_r=GPIO(GPIO.GPIO1, GPIO.OUT)
led_3=GPIO(GPIO.GPIO2, GPIO.OUT)
for x in range(101):
    led_1.value(0)
    time.sleep_ms(100)
    led_1.value(1)
    time.sleep_ms(100)
    led_r.value(0)
    time.sleep_ms(200)
    led_r.value(1)
    time.sleep_ms(200)
    print(x)
    led_3.value(0)
    time.sleep_ms(300)
    led_3.value(1)
    time.sleep_ms(300)
