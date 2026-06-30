# Reverse String
def reverse_string(s):
    print(s[::-1])

# Check pallindrome
def check_palindrome(s):
    print(s == s[::-1])

# find factorial
def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b

# Count vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels in '{s}' is: {count}")
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print(f"Number of vowels in '{s}' is: {count}")


# Find largest of three numbers
def find_largest_number(first, second, third):
    largest = max(first, second, third)
    print(f"The largest number among {first}, {second}, and {third} is: {largest}")

# Check if number is prime
def is_prime(n):
    if n < 2:
        print("Not a prime number")
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
       
def sum_of_digits(n):
    sum = 0
    while n%10 != 0:
        sum += n%10
        n //= 10
    print(f"Sum of digits is: {sum}")

# Main Method
def main():
    reverse_string("Hello, World!")
    check_palindrome("madam")
    print(f"Factorial of 5 is: {fact(5)}")
    fibonacci(10)
    count_vowels("Why do you want to join my organisation?")
    find_largest_number(23,21,22)   
    is_prime(9)
    sum_of_digits(12345)
    find_pairs()

# Find pair of numbers that sum to a target
def find_pairs():
    list = [5,2,8,4,9,3]
    target = 12
    pairs = []
    for i in list:
        for j in list:
            if i + j == target and (j, i) not in pairs and i != j:
                pairs.append((i, j))
    print(f"Pairs that sum to {target} are: {pairs}")

if __name__ == "__main__":
    main()