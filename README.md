# Rubber Ducky Wi-Fi Password Extractor

This project is a Python-based script that simulates keyboard actions to extract saved Wi-Fi passwords on a Windows machine. The script uses PowerShell commands to list and retrieve passwords, stores the information in a text file (`pws.txt`), and then moves the file to a specified directory.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [How it Works](#how-it-works)
- [Usage](#usage)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

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
