# Apollos Eastman
# Nov 4 2024
# Range challenges

import time
#Counting Up & Down
num = int(input('\nInput an integer:\n'))

print()
for i in range(1, num+1):
    print(i)
    time.sleep(.5)

print()
for i in range(num, 0, -1):
    print(i)
    time.sleep(.5)

print('\nWe have lift off!\n')
time.sleep(2)

# Number Cubes
cubes = list(i**3 for i in range(1, 11))
cube_num = 1

for i in cubes:
    print(f'The cube of {cube_num} is {i}.')
    cube_num = cube_num+1
    time.sleep(.5)

time.sleep(2)

# Multiplication Table
num_multi = int(input('\nEnter an integer:\n'))

for i in range(1, num_multi+1):
    print(f'{num_multi} times {i} equals {num_multi*i}')

time.sleep(2)

# List Iteration
total = 0
num_list = list(range(10, 101, 10))
num_elements = len(num_list)

for i in range(num_elements):
    total += num_list[i]

print(f'\nThe sum of the numbers in the list is: {total}\n')
print(f'Double-checking: {sum(num_list)}\n')
