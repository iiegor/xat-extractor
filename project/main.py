import sys

from lib import Commander

if __name__ == '__main__':
    # Define
    commander = Commander()

    # Register
    commander.register('extract <pss/pssa/topsh>')

    # Start listening
    commander.listen()
