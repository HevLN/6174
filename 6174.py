# Kaprekar's constant
# https://www.wikiwand.com/en/6174_(number)
# Take any four-digit number, using at least two different digits (leading zeros are allowed).
# Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.
# Subtract the smaller number from the bigger number.
# Go back to step 2 and repeat.
import time

choiceNumber = int(input(">>> "))
start_time = time.time()
while True:
    split_num = [int(a) for a in str(choiceNumber)]

    descending_order = sorted(split_num, reverse=True)
    ascending_order = sorted(split_num)

    asc = int(''.join(str(i) for i in ascending_order))
    des = int(''.join(str(i) for i in descending_order))

    subtract = (des - asc)
    print(des, "-", asc, "=", subtract)
    choiceNumber = subtract
    if subtract == 6174 or subtract == 495:
        print("--- %s seconds ---" % (time.time() - start_time))
        break


# --- 0.0019526481628417969 seconds ---
# --- 0.0009765625 seconds ---