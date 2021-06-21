import RPi.GPIO as GPIO

# Led Pinout
livingroom = 27
big_bedroom = 17
small_bedroom = 18
bathroom = 22
kitchen = 23
outside = 24

# Switch Pinout
livingroom_button = 21
big_bedroom_button = 20
small_bedroom_button = 26
bathroom_button = 16
kitchen_button = 19
outside_button = 13

# Gate Pinout
gate = False
gate_led = 4
gate_button = 25
gate_closed = 6
gate_opened = 12

# Sensor Pinout
light = 5

# GPIO Header
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(light, GPIO.IN)

GPIO.setup(gate_button, GPIO.IN)
GPIO.setup(gate_led, GPIO.OUT)
GPIO.setup(gate_closed, GPIO.IN)
GPIO.setup(gate_opened, GPIO.IN)

GPIO.setup(livingroom, GPIO.OUT)
GPIO.setup(big_bedroom, GPIO.OUT)
GPIO.setup(small_bedroom, GPIO.OUT)
GPIO.setup(bathroom, GPIO.OUT)
GPIO.setup(kitchen, GPIO.OUT)
GPIO.setup(outside, GPIO.OUT)

GPIO.setup(livingroom_button, GPIO.IN)
GPIO.setup(big_bedroom_button, GPIO.IN)
GPIO.setup(small_bedroom_button, GPIO.IN)
GPIO.setup(bathroom_button, GPIO.IN)
GPIO.setup(kitchen_button, GPIO.IN)
GPIO.setup(outside_button, GPIO.IN)

def magic():
    print("Magic")
    # TODO open/close gate

def changestate(pin):
    if GPIO.input(pin) == 1:
        GPIO.output(pin, 0)
    else:
        GPIO.output(pin, 1)

while True:

    # Gestione Pulsanti illuminazione
    if GPIO.input(livingroom_button) == 1:
        changestate(livingroom)

    if GPIO.input(big_bedroom_button) == 1:
        changestate(big_bedroom)

    if GPIO.input(small_bedroom_button) == 1:
        changestate(small_bedroom)
    
    if GPIO.input(bathroom_button) == 1:
        changestate(bathroom)

    if GPIO.input(kitchen_button) == 1:
        changestate(kitchen)

    if GPIO.input(outside_button) == 1:
        changestate(outside)

    # Gestione Pulsante cancello
    '''
    print (GPIO.input(gate_button))
    if GPIO.input(gate_button) == 1:
        magic()
    '''

    # Gestione fotosensore
    '''
    if GPIO.input(light) == False:
        GPIO.output(outside, True)

    if GPIO.input(light) == True:
        GPIO.output(outside, False)
    '''
