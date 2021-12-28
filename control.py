from pyfirmata import Arduino, SERVO

port='COM3'
pin=8
board=Arduino(port)
board.digital[pin].mode=SERVO
#led_13 = board.get_pin('d:13:o')

def rotateServo(pin,angle):
    board.digital[pin].write(angle)

def barricade(val):
    if val==1:
        rotateServo(pin,90)
    elif val==0:
        rotateServo(pin,0)







