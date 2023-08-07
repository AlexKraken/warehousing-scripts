class SKU_Logger:
    """ Create a SKU logger.

    This SKU logger can create/open a log file, load any previous SKUs 
    into the program, check if a SKU is already logged, and write new 
    SKUs into the log file. 

    """
        
    def __init__(self, log_file: str):
        # Use a set to enforce uniqueness
        self.item_log = set()
        self.log_file = log_file
        
        # Import the log file
        try:
            self.import_log(self.log_file, self.item_log)
        except FileNotFoundError:
            create_new_file = input("File not found, create new file? [y/n]: ")
            if(create_new_file.lower() == 'y'):
                open(self.log_file, 'a').write("SKUs\n")

    def add(self) -> None:
        with open(self.log_file, 'a') as log_writer:
            barcode = input("Scan barcode\n").strip()
            log_writer.write(barcode + "\n")
            self.item_log.add(barcode)
    
    def check(self) -> None:
        looping = True
        while(looping):
            barcode = input("Scan barcode (type in 'exit' when done):\n").strip()
            if barcode.lower() == "exit":
                looping = False
                continue
            if barcode in self.item_log:
                print("PREVIOUSLY FIXED\n")
            else:
                print("NOT FOUND\n")

    def import_log(self, log_file: str, item_log) -> None:
        with open(log_file, 'r') as log_reader:
            for barcode in log_reader:
                item_log.add(barcode.strip())
