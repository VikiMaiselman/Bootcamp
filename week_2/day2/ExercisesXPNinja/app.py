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

# Exc. 3

paragraph = """Friendship contrasted solicitude insipidity in introduced literature it. He seemed denote except as oppose do spring my. Between any may mention evening age shortly can ability regular. He shortly sixteen of colonel colonel evening cordial to. Although jointure an my of mistress servants am weddings. Age why the therefore education unfeeling for arranging. Above again money own scale maids ham least led. Returned settling produced strongly ecstatic use yourself way. Repulsive extremity enjoyment she perceived nor.Perpetual sincerity out suspected necessary one but provision satisfied. Respect nothing use set waiting pursuit nay you looking. If on prevailed concluded ye abilities. Address say you new but minuter greater. Do denied agreed in innate. Can and middletons thoroughly themselves him. Tolerably sportsmen belonging in september no am immediate newspaper. Theirs expect dinner it pretty indeed having no of. Principle september she conveying did eat may extensive"""

chars = len(paragraph)
sentences = len(paragraph.split("."))
words_len = len(paragraph.split(" "))
words = paragraph.split(" ")

unique_words = list(set(words))
non_unique_words = words_len - len(unique_words)
print(f"This very long string contains {chars} characters, {sentences} sentences, {words_len} words and {len(unique_words)} unique words!")

non_unique_words = words_len - len(unique_words)
print(non_unique_words)

non_whitespace_chars = [i for i in paragraph if not i.isspace()]
print(len(non_whitespace_chars))

#Bonus: The average amount of words per sentence in the paragraph.
sentences = paragraph.split(".")
words_averages = [len(sentence.split(' ')) for sentence in sentences]
print(f"There are {round(sum(words_averages) / len(words_averages))} words in each sentence on average")


# Exc. 4
user_input = input("Please, tell us something: ")
user_input = user_input.split(" ")
words_dict = {}

for word in user_input:
    print(not words_dict.get(word))
    words_dict[word] = 1 if not words_dict.get(word) else words_dict[word] + 1

print(words_dict)