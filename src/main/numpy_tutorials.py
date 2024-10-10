import numpy as np


def learn_array():
    numerical_array = np.array([[1, 2, 3-6j, 4], [6, 8, 5, 9]], dtype=complex)
    print(numerical_array)


def main():
    learn_array()


if __name__ == main():
    main()
