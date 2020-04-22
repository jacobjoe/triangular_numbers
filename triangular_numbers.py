"""   Triangular numbers   """

# import time module
import time

# greet user
print('Welcome to "Triangular numbers"')
time.sleep(0.5)

# get input from user
first = int(input("Enter the starting number "))
time.sleep(0.5)
last = int(input("Enter the last number "))
time.sleep(0.5)

# declare dummy variable
k = 0

# loop for adding natural numbers
for j in range(first, last+1):
    k = k + j
    lst = []

    # loop for finding factor of k
    for i in range(1, k+1):
        if k % i == 0:
            lst.append(i)

    # print statement
    print(k, ":", lst)
    time.sleep(0.5)
