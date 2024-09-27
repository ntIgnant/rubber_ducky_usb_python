# Rubber Ducky Wi-Fi Password Extractor

This project is a Python-based script that simulates keyboard actions to extract saved Wi-Fi passwords on a Windows machine. The script uses PowerShell commands to list and retrieve passwords, stores the information in a text file (`pws.txt`), and then moves the file to a specified directory.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [How it Works](#how-it-works)
- [Usage](#usage)
- [Known Issues](#known-issues)

## Project Overview

This project mimics the behavior of a "Rubber Ducky" — a USB device that acts like a keyboard to perform automated tasks on a computer. In this case, the task is to retrieve stored Wi-Fi passwords on the machine using `netsh wlan` and PowerShell commands, and save them in a `.txt` file, which can then be moved to another directory.

## Requirements

- Python 3.x
- Python packages:
  - `keyboard`
  - `time`
  - `os`
  - `getpass`
  
Install the required Python libraries:
```bash
pip install keyboard
```

## Instalation
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/rubber-ducky-wifi-extractor.git
  ```
Navigate to the project directory:
```bash
cd rubber-ducky-wifi-extractor
```
Install the required Python libraries:
```bash
pip install -r requirements.txt
```
Ensure that Python and PowerShell are installed on your machine and that Python is added to your system’s PATH.

## How it Works
The script simulates the following sequence of events:

1. Opens the Windows Run dialog using the Windows + R shortcut or Normal application.
2. Opens a PowerShell session by typing "pwsh" (if PowerShell is installed).
3. Changes the directory to 'Pictures' (can be changed if needed).
4. Executes a PowerShell command (netsh wlan show profile) to get the Wi-Fi profiles stored on the system.
5. For each Wi-Fi profile, it retrieves the password by extracting the Key Content from the netsh command output.
6. The extracted profiles and passwords are saved in a file (pws.txt).
7. The file is moved to the D: drive as specified (NOTE: The name of the disk needs to be changed depending on the user usb name).
8. The PowerShell window is closed using Alt + F4.

## Usage
To run the script, follow these steps:

1. Copy the script into a USB drive.
2. Ensure you have keyboard and other required libraries installed.
3. Run the Python script:
```bash
python3 rubber_ducky_wifi_extractor.py
```
4. After execution, the Wi-Fi profile details and passwords will be stored in pws.txt, which will be moved to the D: drive (or any directory you specify).

## Known Issues
- Admin Privileges: Running the script on a system without admin privileges will result in failure to access Wi-Fi profiles.
- Keyboard Timing: If the system is slow, you may need to adjust the sleep timers for different parts of the script.
