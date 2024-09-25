import win32com.client
import time
import logging
import argparse

# Dictionary for mapping friendly names to dead key characters
DEAD_KEYS = {
    "shift": "+",
    "alt": "%",
    "ctrl": "^",
    "capslock": "{CAPSLOCK}"
}

def press_dead_key(interval, key):
    """
    Presses the specified dead key at regular intervals indefinitely.

    Args:
        interval (int): Time in seconds between key presses.
        key (str): The key to be pressed, as recognized by `SendKeys`.
    """
    shell = win32com.client.Dispatch("WScript.Shell")
    
    while True:
        shell.SendKeys(key)  # Simulates the press of the specified key
        logging.info(f"{key} key pressed")
        time.sleep(interval)


def main():
    """
    Main entry point of the script. Parses command-line arguments, configures logging, and starts key pressing.
    """
    # Setting up argument parser for command-line parameters
    parser = argparse.ArgumentParser(description="Simulate pressing a dead key at regular intervals.")
    parser.add_argument(
        "--interval", 
        type=int, 
        default=60, 
        help="Time interval between key presses in seconds (default: 60)"
    )
    parser.add_argument(
        "--key", 
        type=str, 
        default="shift", 
        choices=DEAD_KEYS.keys(), 
        help="The dead key to press (choices: shift, alt, ctrl, capslock). Default is 'shift'."
    )

    args = parser.parse_args()

    # Configuring basic logging to standard output
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Getting the correct key character from DEAD_KEYS dictionary
    dead_key = DEAD_KEYS[args.key]

    # Starting the key pressing function with the provided interval and key
    press_dead_key(args.interval, dead_key)


if __name__ == "__main__":
    main()
