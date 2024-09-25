# 🖱️ Dead Key Presser

> 🖱️ **Dead Key Presser** is a Python script for simulating dead key presses (such as SHIFT, ALT, CTRL, or CAPS LOCK) at regular intervals on Windows.

## Table of contents

- [Synopsis](#synopsis)
- [Requirements](#requirements)
- [Get started](#get-started)
- [Command-line options](#command-line-options)
- [Run and Test](#run-and-test)
- [Credits](#credits)
- [License](#license)

## Synopsis <a name="synopsis"></a>

**Dead Key Presser** is a tool that simulates pressing a "dead key" on your keyboard at regular intervals. It can simulate keys like SHIFT, ALT, CTRL, and CAPS LOCK, which are useful for keeping a session active or for automation purposes. This script is designed to work **only on Windows** using the `win32com` library for interacting with the Windows environment.

## Requirements <a name="requirements"></a>

- **Windows OS** (the script uses Windows-specific APIs)
- **Python 3.x**
- **pywin32** (Python library for Windows COM objects)

You can install the necessary dependencies using:

```bash
pip install pywin32
```

## Get started <a name="get-started"></a>

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-repo/dead-key-presser.git
   cd dead-key-presser
   ```

2. Install the required Python dependencies:

   ```bash
   pip install pywin32
   ```

3. Run the script to simulate pressing the SHIFT key every 60 seconds:

   ```bash
   python shift_key_presser.py --interval 60 --key shift
   ```

## Command-line options <a name="command-line-options"></a>

The script provides several options to configure the behavior:

- `--interval`: Set the time interval (in seconds) between key presses. Default is 60 seconds.
- `--key`: Choose which dead key to simulate. Available choices are:
  - `shift`: Left SHIFT key (default)
  - `alt`: ALT key
  - `ctrl`: CTRL key
  - `capslock`: CAPS LOCK key

### Examples:

1. Simulate pressing the ALT key every 30 seconds:

   ```bash
   python shift_key_presser.py --interval 30 --key alt
   ```

2. Simulate pressing the CAPS LOCK key every 90 seconds:

   ```bash
   python shift_key_presser.py --interval 90 --key capslock
   ```

## Run and Test <a name="run-and-test"></a>

To run and test the script:

1. After installing the dependencies, you can run the script using the provided command-line options.
2. To test, open a text editor, run the script, and observe the simulated key presses.
3. Adjust the `--interval` and `--key` parameters to test different configurations.

## Credits <a name="credits"></a>

Created by [François-Xavier Michaud](https://github.com/fmichaud).  
You can connect with me on [LinkedIn](https://fr.linkedin.com/in/francoisxaviermichaud).

## License <a name="license"></a>

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

(c) 2023, François-Xavier Michaud
