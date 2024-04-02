#Flask Application Template
from flask import Flask, render_template
from flask_ask import Ask, statement
from time import sleep #Sleep Delay 
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

#Stepper motor GPIO Pins
DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation

#Set mode and pins as input/output
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

#Motor Variables and function
delay = .009 #Motor rotational speed 
previous_position = 0 #Varaible for previous position
total_step_count = 4980 #Time motor stays running; 830 per position

#Step count per position
pos1 = 0
pos2 = 830
pos3 = 1660
pos4 = 2490
pos5 = 3320
pos6 = 4150
pos7 = 4980

#Flask Application Template Continued
app = Flask(__name__)
ask = Ask(app, "/")

def turn_motor():
    for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

#Ask Alexa to open My Blinds, states welcome message
@ask.launch
def start_skill():
    welcome_message = "What position would you like to set your blinds?"
    return question(welcome_message)

#Position intent, this is our answer to the welcome message
@ask.intent('PositionIntent', convert ={'one': int, 'two': int, 'three': int,
                                        'four': int, 'five': int, 'six': int,
                                        'seven': int})

def position():

    if [1]:
            if (1 < previous_position):  
                step_count = abs(pos1 - previous_position)
                turn_motor()
                previous_position = pos1
            else:
                GPIO.output(DIR, CCW)
                step_count = abs(pos1 - previous_position)
                turn_motor()
                previous_position = pos1
            GPIO.cleanup()

    elif [2]:
            if (2 < previous_position):
                turn_motor()
                step_count = abs(pos2 - previous_position)
                previous_position = pos2
            else:
                GPIO.output(DIR, CCW)
                turn_motor()
                step_count = abs(pos2 - previous_position)
                previous_position = pos2
            GPIO.cleanup()

    elif [3]:
            if (3 < previous_position):
                turn_motor()
                step_count = abs(pos3 - previous_position)
                previous_position = pos3
            else:
                GPIO.output(DIR, CCW)
                turn_motor()
                step_count = abs(pos2 - previous_position)
                previous_position = pos3
            GPIO.cleanup()
    elif [4]:
            if (4 < previous_position):
                turn_motor()
                step_count = abs(pos4 - previous_position)
                previous_position = pos4
            else:
                GPIO.output(DIR, CCW)
                turn_motor()
                step_count = abs(pos4 - previous_position)
                previous_position = pos4
            GPIO.cleanup()

    elif [5]:
            if (5 < previous_position):
                turn_motor()
                step_count = abs(pos5 - previous_position)
                previous_position = pos5
            else:
                GPIO.output(DIR, CCW)
                turn_motor()
                step_count = abs(pos5 - previous_position)
                previous_position = pos5
            GPIO.cleanup()

    elif [6]:
            if (6 < previous_position):
                turn_motor()
                step_count = abs(pos6 - previous_position)
                previous_position = pos6
            else:
                GPIO.output(DIR, CCW)
                turn_motor()
                step_count = abs(pos6 - previous_position)
                previous_position = pos6
            GPIO.cleanup()

    elif [7]:
            if (7 < previous_position):
                turn_motor()
                step_count = abs(pos7 - previous_position)
                previous_position = pos7
            else:
                GPIO.output(DIR, CCW)
                turn_motor()
                step_count = abs(pos7 - previous_position)
                previous_position = pos7
            GPIO.cleanup()

    else:
        msg = "Position not valid, choose a position between 1 and 7"
        return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
