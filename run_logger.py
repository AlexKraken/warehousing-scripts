"""Run the barcode logger

Run from the terminal - when prompted, enter the name of an existing log file 
to import previously logged barcodes, or enter a name for a new file:

    > python run_logger.py
    Enter log file name: barcodes.csv
    File not found, create a new file? [y/n]: y

The program will prompt with options:

    Available commands [add/check/exit]: 

    - - -

    add:
        Use to add a new barcode to the log. Returns 'LOG SUCCESSFUL' if it was not
        previously entered, else returns 'ALREADY LOGGED'.

    check:
        Use to check if a barcode has already been logged. Returns 'BARCODE FOUND'
        if it was previously entered, else returns 'NOT FOUND'. This will continue
        prompting for another barcode until the user enters 'exit'.

    exit:
        Use to exit the program and return to the command line.

"""

from barcode_logger import BarcodeLogger

log_file = input("Enter log file name: ").strip()

try:
    logger = BarcodeLogger(log_file)
except FileNotFoundError:
    create_new_file = input("File not found, create new file? [y/n]: ").strip().lower()
    if create_new_file == "y":
        with open(log_file, "a") as file:
            file.write("Barcodes\n")
        logger = BarcodeLogger(log_file)
    else:
        raise SystemExit("Exiting - check the filename and run again")

while True:
    user_input = input("Available commands [add/check/exit]: ").strip().lower()

    match user_input:
        case "add":
            logger.add()
        case "check":
            logger.check()
        case "exit":
            break
        case _:
            continue
