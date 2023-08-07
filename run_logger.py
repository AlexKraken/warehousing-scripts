from sku_logger import SKULogger

try:
    logger = SKULogger(input("Enter log file name: "))
except FileNotFoundError:
    print("File not found - check the name and try running again")
else:
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
