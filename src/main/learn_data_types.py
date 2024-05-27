import logging
import math

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

#Setting Logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

#This is text type data
logger.info("Testing Text datatype!")
name = 'Vikhyat Srivastava'
place_of_work = "London"

print("My name is", name)
print("My work place is", place_of_work)

#This is numeric type data
logger.info("Testing numeric datatype!")
int_num = 100
float_num = 100.20
complex_num_1 = (2 + 5j)
complex_num_2 = (1 - 1j)
logger.info("Testing int, float and complex type and operations among int, float and complex data!")
#1. Int
print("This is int data", int_num)
print("Sum of two int data i.e", int_num, "and 5 is", int_num + 5)
#2. Float
print("This is float data", float_num)
print("Product of two float data i.e", float_num, " and 4.2 is", float_num * 4.2, ". Round of result is",
      round(float_num * 4.2, 2))
#3. Complex Number
print("This is complex number", complex_num_1)
print("Product of two complex data i.e", complex_num_1, " and", complex_num_2, " is", complex_num_1 * complex_num_2)

#This is sequence type data
#1. List
logger.info("Testing sequence datatype!")
my_list = ["Citi", "LBG", "Roche", "LBG"]
my_tuple = ("Cricket", "Badminton", "BasketBall", "BaseBall", "FootBall", "Cricket")
my_range = range(10)
my_dictionary={"language": "Python", "version": "3.6"}
logger.info("Testing list, tuple, dictionary and range type and operations among list, tuple, dictionary and range "
            "data!")
print("This is my list", my_list, ". Lists are mutable i.e. changeable, ordered and allow duplicates.")
my_list.append("Awaited")
print("This is my list with added element", my_list)
my_list.remove("Awaited")
print("This is my list with removed element", my_list)
#2. Tuple
print("This is my tuple", my_tuple, ". Tuples are immutable i.e. unchangeable, ordered and allow duplicates.")
#3. Dictionary
print("This is my dictionary", my_dictionary, ". Dictionary are mutable i.e. changeable, unordered (3.6)/ordered ("
                                              "3.7+) and doesn't allows duplicates.")
print("Language in my_dictionary is", my_dictionary["language"])
my_dictionary["release_date"] = "22 Dec 2016"
print("This is my_dictionary after adding release_date", my_dictionary)
my_dictionary.update({"version" : "3.6.0"})
print("This is my_dictionary after updating version", my_dictionary)
my_dictionary.pop("release_date")
print("This is my_dictionary after removing release_date", my_dictionary)
#4. Range
print("This is my range", my_range, ". Range is a function to get the continuous (int) numbers between two end points")
print("This is my range between 10 to 5", range(10, 5))
print("This is my range between 1 to 5", range(1, 5))
print("This is my range between -3 to 8", range(-3, 8))