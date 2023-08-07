class SKULogger:
    """Create a SKU logger.

    This SKU logger can create/open a log file, load any previous SKUs
    into the program, check if a SKU is already logged, and write new
    SKUs into the log file.

    """

    def __init__(self, log_file: str):
        # Use a set to enforce uniqueness
        self.log_file = log_file
        self.sku_log = set()

        # Import the log file
        try:
            with open(log_file, "r") as log_reader:
                for barcode in log_reader:
                    self.sku_log.add(barcode.strip())
        except FileNotFoundError:
            create_new_file = input("File not found, create new file? [y/n]: ")
            if create_new_file.lower() == "y":
                open(self.log_file, "a").write("SKUs\n")
            else:
                raise FileNotFoundError

    def add(self) -> None:
        with open(self.log_file, "a") as log_writer:
            barcode = input("Scan barcode\n").strip()
            log_writer.write(barcode + "\n")
            self.sku_log.add(barcode)

    def check(self) -> None:
        looping = True
        while looping:
            barcode = input("Scan barcode (type in 'exit' when done):\n").strip()
            if barcode.lower() == "exit":
                looping = False
                continue
            if barcode in self.sku_log:
                print("PREVIOUSLY FIXED\n")
            else:
                print("NOT FOUND\n")
