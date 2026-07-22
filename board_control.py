from pyfirmata import *

board = Arduino("/dev/cu.usbmodem101")


def superposition(pin):
    qb = board.digital[pin]
    qb.mode = PWM
    qb.write(0.1)


def write(pin, value):
    qb = board.digital[pin]
    qb.write(value)


if __name__ == "__main__":
    board.digital[11].mode = PWM
    board.digital[11].write(0.05)
