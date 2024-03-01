import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Define the pins connected to VRx, VRy, and SW
PIN_X = 17  # Replace with the actual GPIO pin number for X axis
PIN_Y = 18  # Replace with the actual GPIO pin number for Y axis
PIN_SW = 27  # Replace with the actual GPIO pin number for the switch

# Set up the GPIO pins
GPIO.setup(PIN_X, GPIO.IN)
GPIO.setup(PIN_Y, GPIO.IN)
GPIO.setup(PIN_SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use pull-up resistor

try:
    while True:
        # Read analog values
        x_value = GPIO.input(PIN_X)
        y_value = GPIO.input(PIN_Y)

        # Read the button state
        button_state = GPIO.input(PIN_SW)

        # Print the values and button state
        print(f"X: {x_value}, Y: {y_value}, Button: {button_state}")

        # Add a delay to prevent excessive printing
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
