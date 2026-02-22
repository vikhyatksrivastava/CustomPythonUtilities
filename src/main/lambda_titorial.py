import math

# A regular function
def add_ten(x):
    return x + 10

# The equivalent lambda
lambda_add_ten = lambda x: x + 10

print(f"""Value of lambda_add_ten(5): {lambda_add_ten(5)}""") # Output: 15

def find_factorial(n):
    if n == 0:
        return 1
    else:
        return n * find_factorial(n - 1)

temp = 6
factorial_altered = lambda n: find_factorial(n) * math.ceil(math.pow(n,3))
factorial_with_temp = find_factorial(temp)
print(f"""Factorial of {temp} using lambda: {factorial_altered(temp)}""") # Output: 720
print(f"""Factorial of {temp} using temp variable: {factorial_with_temp}""") # Output: 720