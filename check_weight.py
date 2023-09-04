"""For now, this script is meant to be used from Python's interactive shell
    to complement the other basic calculations that are commonly used:

    >>> from check_weight import check
    >>> check()

    Example:
        Suppose an item's weight is measured to be 0.11 lbs, and the system has the
        weight as 1 lb. While in Python's interactive shell, run:

        >>> check()
        Enter the expected weight (in lbs): 1
        Enter the measured weight (in lbs): 0.1
        -----
        Absolute error:   0.90 lbs
        Percentage error: 900%

"""


def check_weight(expected_weight: float, measured_weight: float) -> tuple:
    """Calculates various errors of an item's weight relative to what's in the system

    For fixing incorrect weights in the system, percentage error is defined as:
    Percentage Error = ((Expected Weight - Measured Weight) / Measured Weight) x 100%

    For example:

        Suppose an item's weight is measured to be 0.25 lbs
        The system expects the item's weight to be 1.50 lbs
        The percentage error is (1.50 - 0.25)/0.25 x 100% = 500%

        A 500% error means the system's expectation is 5 times OVER the actual weight,
        suggesting that the previous measurement could have been made on a case pack
        of 6 units, or the item was mistakenly taken out of a case pack
        _ _ _ _ _ _ _

        Suppose a case pack of 10 items is measured to be 1.20 lbs
        The system expects the case pack to weigh 0.12 lbs
        The percentage error is (0.12 - 1.20)/0.12 x 100% = -900%

        A -900% error means the system's expectation is 9 times UNDER the measured
        weight, which suggests that either the case pack isn't how the item should
        be sold, or that the previous measurement was made by mistakenly taking an item
        out of its case pack.

    """

    absolute_error = expected_weight - measured_weight
    percentage_error = (absolute_error / measured_weight) * 100

    return absolute_error, percentage_error


def check() -> None:
    """This function basically provides prompts the user for the inputs, allowing quick
        entry with a numpad, and calls check_weight() and prints the formatted results. 

    """

    expected_weight = float(input("Enter the expected weight (in lbs): "))
    measured_weight = float(input("Enter the measured weight (in lbs): "))

    absolute_error, percentage_error = check_weight(expected_weight, measured_weight)

    print("-----")
    print(f"Absolute error:   {absolute_error:.2f} lbs")
    print(f"Percentage error: {percentage_error:.0f}%")
