from machine import PWM, Pin


pwm = PWM(Pin(16))
pwm.duty_u16(32768)

pwm.init(freq=5000, duty_ns=5000)