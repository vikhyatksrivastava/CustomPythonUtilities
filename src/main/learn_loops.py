import logging

#Setting Logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


my_list = ["Citi", "LBG", "Roche", "LBG"]
my_tuple = ("Cricket", "Badminton", "BasketBall", "BaseBall", "FootBall", "Cricket")
my_range = range(10)
my_dictionary = {"language": "Python", "version": "3.6"}

def test_for_loop_on_list():
    logger.info("Testing For Loop on List.")
    for entry in my_list:
        print(f"{entry}")


def test_for_loop_on_tuple():
    logger.info("Testing For Loop on Tuple.")
    for entry in my_tuple:
        print(f"{entry}")


def test_for_loop_on_dictionary():
    logger.info("Testing For Loop on Dictionary.")
    for entry in my_dictionary:
        print(f"{entry}")


def test_for_loop_on_range():
    logger.info("Testing For Loop on Range.")
    for entry in my_range:
        print(f"{entry}")


def test_while_loop():
    i = 0
    while i < 10:
        print(i * 10)
        i += 1


def test_while_on_range():
    i = 0
    while i not in my_range:
        if i % 2 == 0:
            print(f"{i} is even number")

def main():
    test_for_loop_on_list()
    test_for_loop_on_tuple()
    test_for_loop_on_dictionary()
    test_for_loop_on_range()
    test_while_loop()
    test_while_on_range()

if __name__ == '__main__':
    main()
