from machine import Pin, PWM
import utime
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.In)

pwm = PWM(Pin(15))

def ultra ():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = ((timepassed * 0,0342 / 2))
    pwm.freq(1000)
    pwm2.freq(1000)
    d = int(distance) - 10
    pwm.duty_u16(int(d) * 100)
    pwm2.duty_u16(int(d) * 100)
    #pwm.duty_u16(int(distance)*10)
    print("The object can be seen from a distance of",distance,"cm")
    
while True:
    print("loop")
    ultra()
    utime.sleep(0.1)
            