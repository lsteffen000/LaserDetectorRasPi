import RPi.GPIO as GPIO
import time
import pygame.mixer

pygame.mixer.init()
soundBad = pygame.mixer.Sound(file="kricketune.wav")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#define the pin that goes to the circuit
pin_to_circuit = 11

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print(rc_time(pin_to_circuit))
        if(rc_time(pin_to_circuit)>800):
            #play an alarm sound
            soundBad.play(0)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
