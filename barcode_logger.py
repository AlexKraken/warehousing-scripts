class BarcodeLogger:
    """Create a barcode logger

    This barcode logger will open a log file, load any previous barcodes
    into the program, check if a barcode has already been logged, and write
    new barcodes into the log file.

    """

    def __init__(self, log_file: str) -> None:
        # Use a set to enforce uniqueness
        self.barcode_log = set()
        self.log_file = log_file

        # Import the log file
        with open(log_file, "r") as log_reader:
            for barcode in log_reader:
                self.barcode_log.add(barcode.strip())

    def add(self) -> None:
        with open(self.log_file, "a") as log_writer:
            barcode = input("Scan barcode\n").strip()

            if barcode not in self.barcode_log:
                log_writer.write(barcode + "\n")
                self.barcode_log.add(barcode)
                print("LOG SUCCESSFUL\n")
            else:
                print("ALREADY LOGGED\n")

    def check(self) -> None:
        while True:
            barcode = input("Scan barcode (type in 'exit' when done):\n").strip().lower()

            if barcode == "exit":
                break

            if barcode in self.barcode_log:
                print("BARCODE FOUND\n")
            else:
                print("NOT FOUND\n")
