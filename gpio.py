import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO_PIN = 24  # GPIO pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(channel):
    print("Button pressed on GPIO pin", channel)

# Add event detection for GPIO button press
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
    print("Waiting for button press. Press Ctrl+C to exit.")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nExiting.")
