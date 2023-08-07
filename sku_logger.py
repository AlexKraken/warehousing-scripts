class SKULogger:
    """Create a SKU logger.

    This SKU logger will open a log file, load any previous SKUs
    into the program, check if a SKU has already been logged, and write new
    SKUs into the log file.

    """

    def __init__(self, log_file: str):
        # Use a set to enforce uniqueness
        self.log_file = log_file
        self.sku_log = set()

        # Import the log file
        with open(log_file, "r") as log_reader:
            for barcode in log_reader:
                self.sku_log.add(barcode.strip())

    def add(self) -> None:
        with open(self.log_file, "a") as log_writer:
            barcode = input("Scan barcode\n").strip()
            
            if barcode not in self.sku_log:
                log_writer.write(barcode + "\n")
                self.sku_log.add(barcode)
                print()
            else:
                print("Already entered\n")

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
