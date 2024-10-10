def find_prime_number():
    num = 29
    # num = int(input("Enter a number: "))
    flag = False
    if num == 1:
        flag = False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
            else:
                flag = False
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


def find_factorial():
    input_num = 7
    # input_num = int(input("Write Input Number: "))
    fact = 1
    i = 1
    for i in range(1, input_num+1):
        fact = fact * i
    print("factorial of", input_num, "is", fact)


def main():
    # findPrimeNumber()
    find_factorial()


if __name__ == main():
    main()
