from sku_logger import SKULogger

logger = SKULogger(input("Enter log file name: "))


while True:
    user_input = input("Availible commands [add/check/exit]: ").strip().lower()

    match user_input:
        case "add":
            logger.add()
        case "check":
            logger.check()
        case "exit":
            break
        case _:
            continue
