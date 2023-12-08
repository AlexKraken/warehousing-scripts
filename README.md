# warehousing-scripts
These are scripts used to make QA's job a little easier. They started out as scripts to be used from the terminal and Python's interactive shell, but now include a website for those more comfortable with a web browser.


## Barcode Logger
This is useful for quickly checking whether or not a particular item has been logged before. Since any changes to a item's specifications won't be in effect until the next day, this log is useful for catching errors that have already been fixed but will still be flagged until the system updates.

Run from the terminal - when prompted, enter the name of an existing log file to import previously logged barcodes, or enter a name for a new file:

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


## Weight Checker
This allows for quickly checking how far off the system's entry on an item's weight is from the actual amount. 

For now, this script is meant to be used from Python's interactive shell to complement the other calculations that are commonly used:

    >>> from check_weight import check
    >>> check()


##### Example:
Suppose an item's weight is measured to be 0.1 lbs, and the system has the weight as 1 lb. While in Python's interactive shell, run:

    >>> check()
    Enter the expected weight (in lbs): 1
    Enter the measured weight (in lbs): 0.1
    -----
    Absolute error:   0.90 lbs
    Percentage error: 900%


### The Math
For fixing incorrect weights in the system, percentage error is defined as:
```math
\text{Percentage Error} = \frac{{\text{Expected Weight} - \text{Measured Weight}}}{{\text{Measured Weight}}} \times 100\%
```


##### Example:
Suppose an item's weight is measured to be 0.25 lbs but the system expects the item's weight to be 1.50 lbs.

```math
\text{Percentage Error} = \frac{{1.50 - 0.25}}{{0.25}} \times 100\% = 500\%
```

A 500% error means the system's expectation is 5 times OVER the actual weight, suggesting that the previous measurement could have been made on a case pack of 6 units, or the current item was mistakenly taken out of a case pack.


##### Example:
Suppose a case pack of 10 items is measured to be 1.20 lbs but the system expects the case pack to weigh 0.12 lbs.

```math
\text{Percentage Error} = \frac{{0.12 - 1.20}}{{0.12}} \times 100\% = -900\%
```

A -900% error means the system's expectation is 9 times UNDER the measured weight, which suggests that either the case pack isn't how the item should be sold, or that the previous measurement was made by mistakenly taking an item out of its case pack.
