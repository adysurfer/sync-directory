# sync-directory
A program that synchronizes two directories: source and replica;

#############################################

Program: sync-directory

Created on: 21<sup>st</sup> Sep 2022

Last Modified on Python 3.x.x: 24<sup>th</sup> Sep 2022

Last Updated By: Aditya

##############################################

**Features:**
- Periodically one-way synchronization, identical copy of source directory is maintained in replica directory;
- File creation/copying/removal operations are logged to a file and to the console output;
- Directory path, synchronization interval and log file path are provided using the command line arguments;

**Log File Preview:**

<img width="700" alt="Screenshot 2022-09-24 at 13 44 11" src="https://user-images.githubusercontent.com/5576793/192096150-f77ba466-7b8d-409e-bfc3-deb229f44395.png">


**Project Structure:**

*Main Application:*
- sync_dir.py

*Others:*

- README.md

**Modules:**

- hashlib
- os
- shutil
- sys
- time
- logging

**Steps for execution:**
- `git clone https://github.com/adysurfer/sync-directory.git`
- Run using `python3 sync_dir.py <path-to-log-file> <synchronization interval in seconds>`
