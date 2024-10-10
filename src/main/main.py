# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    my_list = [1, 2, 3, 4, 5]
    print(f'mylist have {my_list} before assignment')
    copy_list = my_list
    copy_list.append(6)
    print(f'mylist have {my_list} after assignment')
    print(f'copy_list have {copy_list}')

    numbers = [1, 2, 3, 4, 5]
    target_sum = 5

    # Use a set for efficient lookups
    seen = set()
    for number in numbers:
        complement = target_sum - number
        if complement in seen:
            print(f"Pair found: ({number}, {complement})")
        seen.add(number, complement)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
