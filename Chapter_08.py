#  TRY THIS: LOOPING AND IF STATEMENTS Suppose that you have a list x = [1,
#  3, 5, 0, -1, 3, -2], and you need to remove all negative numbers from
#  that list. Write the code to do this.
#  How would you count the total number of negative numbers in a list
#  y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]? 
# What code would you use to print very low if the value of x is below -5, low
#  if it’s from -5 up to 0, neutral if it’s equal to 0, high if it’s greater than 0 up
#  to 5, and very high if it’s greater than 5? 


# # Remove negative numbers
# x = [num for num in x if num >= 0]
# # Count negative numbers
# negative_count = sum(1 for sublist in y for num in sublist if num < 0)
# # Categorize x based on its value
# if x < -5:
#     print("very low")
# elif -5 <= x < 0:
#     print("low")
# elif x == 0:
#     print("neutral")
# elif 0 < x <= 5:
#     print("high")
# else:
#     print("very high")



# TRY THIS: COMPREHENSIONS What list comprehension would you use to pro
# cess the list x so that all negative values are removed?
#  Create a generator that returns only odd numbers from 1 to 100. (Hint: A
#  number is odd if there is a remainder if divided by 2; use % 2 to get the
#  remainder of division by 2.)
#  Write the code to create a dictionary of the numbers and their cubes from 11
#  through 15.

# x = [1, -3, 5, 0, -2, 4, -1]
# x = [num for num in x if num >= 0]
# #return odd numbers from 1 to 100
# odd_numbers = (num for num in range(1, 101) if num % 2 != 0)
# #dictionary with numbers and their cubes from 11 to 15
# cubes = {num: num**3 for num in range(11, 16)}



# QUICK CHECK: BOOLEANS AND TRUTHINESS Decide whether the following state
# ments are true or false: 
# 1 #True
# 0 #False
# -1 #True
# [0] #True
# 1 and 0 #False
# 1 > 0 or [] #True


#  LAB 8: REFACTOR WORD_COUNT Rewrite the word-count program from section
#  8.7 to make it shorter. You may want to look at the string and list operations
#  already discussed, as well as think about different ways to organize the code.
#  You may also want to make the program smarter so that only alphabetic
#  strings (not symbols or punctuation) count as words.

# import re
# from collections import Counter
# def word_count(filename):
#     with open(filename) as infile:
#         # Read all lines, convert to lowercase, remove non-alphabetic characters, and split into words
#         words = re.findall(r'\b[a-zA-Z]+\b', infile.read().lower())
#     # Count the occurrences of each word
#     word_counts = Counter(words)
#     # Print the word count
#     for word, count in word_counts.items():
#         print(f'{word}: {count}')