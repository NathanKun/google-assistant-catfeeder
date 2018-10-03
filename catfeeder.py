import time
import pigpio

# Servo
PIN             = 12
FEQ_TURN_LEFT   = 306
FEQ_TURN_RIGHT  = 350
FEQ_STOP        = 334 # stop from 321 to 337
TURNING_TIME    = 0.33
START_TURN_TIME = 0.03
DUTY_CYCLE      = 500000

def main():
        pi = pigpio.pi()
        turn(pi, TURNING_TIME)
        pi.stop()

def startTurn(pi):
        for i in range(FEQ_STOP, FEQ_TURN_RIGHT):
                pi.hardware_PWM(PIN, i, DUTY_CYCLE)
                time.sleep(START_TURN_TIME)

def turn(pi, delay):
        startTurn(pi)
        pi.hardware_PWM(PIN, 344, DUTY_CYCLE)
        time.sleep(delay)
        pi.hardware_PWM(PIN, FEQ_STOP, DUTY_CYCLE)

if __name__ == "__main__":
        main()
