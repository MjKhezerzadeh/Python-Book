#  TRY THIS: CREATE A DICTIONARY Write the code to ask the user for three
#  names and three ages. After the names and ages are entered, ask the user for
#  one of the names, and print the correct age.

# age_dict = {}
# for _ in range(3):
#     name = input("Enter a name: ")
#     age = input(f"Enter the age of {name}: ")
#     age_dict[name] = age

# search_name = input("Enter a name to find the age: ")

# if search_name in age_dict:
#     print(f"The age of {search_name} is {age_dict[search_name]}")
# else:
#     print("That name is not in the list.")



#  QUICK CHECK: DICTIONARY OPERATIONS Assume that you have a dictionary x =
#  {'a':1, 'b':2, 'c':3, 'd':4} and a dictionary y = {'a':6, 'e':5,
#  'f':6}. What would be the contents of x after the following snippets of code
#  have executed?: 
# del x['d'] #x = {'a': 1, 'b': 2, 'c': 3}
#  z = x.setdefault('g', 7) #x = {'a': 1, 'b': 2, 'c': 3, 'g': 7}
#  x.update(y) #x = {'a': 6, 'b': 2, 'c': 3, 'g': 7, 'e': 5, 'f': 6}



#  QUICK CHECK: WHAT CAN BE A KEY? Decide which of the following expressions
#  can be a dictionary key: 
# 1; 'bob'; ('tom', [1, 2, 3]); ["file
# name"]; "filename"; ("filename",  "extension")

# Cannot be a key: ('tom', [1, 2, 3]); ["file
# name"];



# TRY THIS: USING DICTIONARIES Suppose that you’re writing a program that
#  works like a spreadsheet. How might you use a dictionary to store the con
# tents of a sheet? Write some sample code to both store a value and retrieve a
#  value in a particular cell. What might be some drawbacks to this approach? 

# spreadsheet = {}
# #store
# spreadsheet["A1"] = 10
# spreadsheet["B2"] = "Hello, world!"
# #retrieve
# spreadsheet.get("A1")
# spreadsheet.get("b1")
# #drawbacks
# #No Row/Column Structure



#  LAB 7: WORD COUNTING In the previous lab, you took the text of the first chap
# ter of Moby Dick, normalized the case, removed punctuation, and wrote the
#  separated words to a file. In this lab, you read that file, use a dictionary to
#  count the number of times each word occurs, and then report the most com
# mon and least common words. 

# with open("moby_dick.txt", "r") as infile:
#     for line in infile:
#         word = line.strip()
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1

# #most common word and count
# most_common_word = max(word_counts, key=word_counts.get)
# most_common_count = word_counts[most_common_word]