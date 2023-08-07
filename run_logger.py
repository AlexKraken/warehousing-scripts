from sku_logger import SKULogger

log_file = input("Enter log file name: ")

try:
    logger = SKULogger(log_file)
except FileNotFoundError:
    create_new_file = input("File not found, create new file? [y/n]: ")
    if create_new_file.lower() == "y":
        with open(log_file, "a") as file:
            file.write("SKUs\n")
        logger = SKULogger(log_file)
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
