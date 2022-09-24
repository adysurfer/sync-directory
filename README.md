# sync-directory
A program that synchronizes two folders: source and replica;

#############################################

Program: sync-directory

Created on: 21<sup>st</sup> Sep 2022

Last Modified on Python 3.x.x: 24<sup>th</sup> Sep 2022

Last Updated By: Aditya

##############################################

**Features:**
- Periodically one-way synchronization, identical copy of source folder is maintained in replica folder;
- File creation/copying/removal operations are logged to a file and to the console output;
- Folder paths, synchronization interval and log file path are provided using the command line arguments;

**Log File Preview:**

<img width="600" alt="Screenshot 2022-09-24 at 11 42 16" src="https://user-images.githubusercontent.com/5576793/192091342-ddbad91e-6172-4bd3-b171-565b6a45e6c0.png">

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
