import math


def calculate_change(amount):
    """Calculates the minimum number of 10, 5, and 2 rupee notes needed to return a given amount.

    Args:
        amount (int): The amount to be returned (in rupees).

    Returns:
        dict: A dictionary containing the number of 10, 5, and 2 rupee notes needed.
    """

    if amount <= 0:
        return {}

    notes = [10, 5, 2]
    change = {}

    for note in notes:
        change[note] = amount // note
        amount %= note

    return change


def main():
    print(calculate_change(1009))


if __name__ == '__main__':
    main()
