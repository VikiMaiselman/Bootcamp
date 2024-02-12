# Exc. 1
# Q = sqrt [(2 * 50 * D) / 30]
import math
import random

results = []
user_input = input("Enter values you want to calculate (comma-separated): ")
user_input = user_input.replace(" ", "") # if the user enters "1, 2,   3,4"
numbers = user_input.split(",")

for num_char in numbers:
    if not num_char.isnumeric():
        print("You entered and invalid number. It won't be included into calculations.")
        continue
    results.append(round(math.sqrt(2 * 50 * int(num_char) / 30)))


print(results)


# Exc. 2
my_list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
my_list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
my_list3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
my_list4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# print list in a single line
print(my_list1)

# sorted descending order
my_list1.sort(reverse=True)
print(my_list1)

# sum of all numbers
sum1 = sum(my_list1)
print(sum1)

# VS
sum2 = 0
for num in my_list1:
    sum2 = sum2 + num

print(sum2)

# another list containing the 1st & the last numbers only
new_list = [my_list2[0], my_list2[-1]]
print(new_list)

# A list of all the numbers greater than 50.
filtered1 = filter(lambda x: x > 50, my_list2)
print(list(filtered1))

#A list of all the numbers less thna 10
filtered2 = filter(lambda x: x < 10, my_list2)
print(list(filtered2))

# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9"
sq_list = [x**2 for x in my_list2]
print(sq_list)

# The numbers without any duplicates – also print how many numbers are in the new list
list_unique = list(set(my_list4))
print(list_unique)
print(len(list_unique))

# average of all numbers in list 
average = sum(my_list4) / len(my_list4)
print(average)

# max number
max_num = max(my_list4)
print(max_num)

min_num = min(my_list4)
print(min_num)

# Find the sum, average, largest and smallest number without using built in functions.

list_total = 0
list_len = 0
max_n = 0
min_n = 0


for num in my_list4:
    list_total = list_total + num
    list_len += 1
    
    if num > max_n:
        max_n = num
        
    if num < min_n:
        min_n = num
    
print(f"Sum = {list_total}, Average = {list_total / list_len}, Max number = {max_n} and Min number = {min_n}")

# ask user for integers
user_list = []
for i in range(10):
    user_num = int(input("Enter an integer between -100 and 100: "))
    if user_num < -100 or user_num > 100:
        print(f"{user_num} won't be included")
        continue
    user_list.append(user_num)

print(user_list)

# generate 10 random integers yourself. Make sure that these random integers are between -100 and 100
my_list = []
for i in range(10):
    my_list.append(random.randint(-100,100))
    
print(my_list)

# random # of list items
my_list = []
for i in range(random.randint(0, 50)):
    my_list.append(random.randint(-100,100))
    
print(my_list)