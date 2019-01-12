import RPi.GPIO as GPIO


BUTTON_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def is_button_pressed():
    return GPIO.input(BUTTON_PIN) == GPIO.HIGH


def set_button_callback(button_callback):
    GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback, bouncetime = 500) # Setup event on pin 10 rising edge

