"""
A program that synchronizes two folders: source and replica;

Features:
> Periodically one-way synchronization, identical copy of source folder is maintained in replica folder;
> File creation/copying/removal operations are logged to a file and to the console output;
> Folder paths, synchronization interval and log file path are provided using the command line arguments;

"""
# Import required dependencies
import hashlib
import os
import shutil
import sys
import time
import logging

# Configure logging
try:
    logging.basicConfig(filename=sys.argv[1], level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S')

except IsADirectoryError as e:
    print(f'{e}\nNot a valid file path')
    sys.exit()

# Get logs in console output
logging.getLogger().addHandler(logging.StreamHandler())


# Compare files in source and replica directories using md5 hash
def compare_files(file_src, file_replica):
    # compare 2 files with hash
    with open(file_src, 'rb') as f1:
        with open(file_replica, 'rb') as f2:
            if hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest():
                return True
            else:
                return False


# Compare source and replica directories
def compare_folders(file_src, file_replica):
    # Get all files from source directory
    files_source = os.listdir(file_src)

    # Get all files from  replica directory
    files_repl = os.listdir(file_replica)

    # Compare src/replica files list
    if len(files_source) != len(files_repl):
        return False

    # Return false if any file is different
    for files in files_source:
        if files in files_repl:
            if not compare_files(file_src + '/' + files, file_replica + '/' + files):
                return False
        else:
            return False
    # Return True if all files are same
    return True


# Input source/replica directories path
source_path = input("Enter source folder path\n")
replica_path = input("Enter replica folder path\n")

# Directories name
source_dirname = "source"
replica_dirname = "replica"

# Check for valid path
is_dirpath1 = os.path.isdir(source_path)
is_dirpath2 = os.path.isdir(replica_path)

# Join path with source/replica directory names
src_dirpath = os.path.join(source_path, source_dirname)
replica_dirpath = os.path.join(replica_path, replica_dirname)

if is_dirpath1 and is_dirpath2:
    # Make source directory if path is valid
    if not os.path.isdir(src_dirpath):
        os.mkdir(src_dirpath)
        print("source directory created")

    else:
        print(f"source directory exist")

    # Make replica directory if path is valid
    if not os.path.isdir(replica_dirpath):
        os.mkdir(replica_dirpath)
        print("replica directory created")

    else:
        print(f"replica directory exist")
# Exit when not valid path is provided in input
else:
    print("Not a valid directory path\nExiting...")
    sys.exit()

# Perform periodic file creation/copying/removal operations
while True:

    # Check source directory existence
    if os.path.isdir(src_dirpath):
        logging.info('source directory status : ONLINE')

    # Delete replica directory if source directory is deleted manually
    else:
        logging.info('source directory deleted on current path\nDeleting existing replica directory\nExiting...\n')
        shutil.rmtree(replica_dirpath, ignore_errors=True)
        break

    # check replica directory existence
    if os.path.isdir(replica_dirpath):
        logging.info('replica directory status : ONLINE')

    # Create replica directory if replica directory is deleted manually
    else:
        logging.info('replica directory does not exist\nCreating replica directory...')
        os.mkdir(replica_dirpath)

    # Check if source directory is in sync with replica
    if compare_folders(src_dirpath, replica_dirpath):
        logging.info('replica directory is in sync with source directory')
    else:
        # Get source directory files
        files_src = os.listdir(src_dirpath)

        # Get replica directory files
        files_replica = os.listdir(replica_dirpath)

        # Compare source and replica directory files
        for file in files_replica:
            if file in files_src:
                if compare_files(src_dirpath + '/' + file, replica_dirpath + '/' + file):
                    logging.info(f'File {file} is up to date')

                else:
                    # Copy files from source to replica directory
                    os.remove(replica_dirpath + '/' + file)
                    os.system('cp ' + src_dirpath + '/' + file + ' ' + replica_dirpath)
                    logging.info(f'File {file} is updated')

            if file not in files_src:
                # Delete files from replica directory
                os.remove(replica_dirpath + '/' + file)
                logging.info(f'File {file} is deleted')

        for file in files_src:
            if file not in files_replica:
                # Copy files from source to replica directory
                os.system('cp ' + src_dirpath + '/' + file + ' ' + replica_dirpath)
                logging.info(f'File {file} is copied')

    # Provide synchronization interval
    try:
        time.sleep(int(sys.argv[2]))

    except ValueError as e1:
        print(f'{e1}\n Not a valid synchronization interval value')
        sys.exit()
