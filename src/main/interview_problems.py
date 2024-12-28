# There are n houses in a village, given ith house gets infected on day 1 and on day 2 (i-1)th and (i+1)th house gets infected then after how many days whole village will be infected.

def calculate_num_of_days(num_of_houses, first_house_to_infect):
    num_of_days = 1
    left_house = first_house_to_infect - 1
    right_house = first_house_to_infect + 1
    for i in range(num_of_houses):
        if left_house > 0 or right_house <= num_of_houses:
            num_of_days += 1
            left_house -= 1
            right_house += 1

    return num_of_days

def main():
    num_of_houses = 10
    first_house_to_infect = 3
    print(f"""It will take {calculate_num_of_days(num_of_houses, first_house_to_infect)} number of days to infect full village of {num_of_houses} families if {first_house_to_infect} house gets infected""")

if __name__ == '__main__':
    main()