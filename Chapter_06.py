# QUICK CHECK: SPLIT AND JOIN How could you use split and join to change
#  all the whitespace in string x to dashes, such as changing "this is a test"
#  to "this-is-a-test"? 

# x = "this is a test"
# modified_string = '-'.join(x.split())



# QUICK CHECK: STRINGS TO NUMBERS Which of the following will not be con
# verted to numbers, and why?
#  int('a1') #ValueError
#  int('12G', 16) #The character 'G' is invalid in base 16
#  float("12345678901234567890")
#  int("12*2") #ValueError



#  QUICK CHECK: STRIP If the string x equals "(name, date),\n", which of
#  the following would return a string containing "name, date"?
#  x.rstrip("),") #"(name, date"
#  x.strip("),\n") #"name, date"
#  x.strip("\n)(,") #"name, date"



# QUICK CHECK: STRING SEARCHING If you wanted to check whether a line ends
#  with the string "rejected", what string method would you use? Would there
#  be any other ways to get the same result?

# line = "The application was rejected"
# if line.endswith("rejected"):
#     print("The line ends with 'rejected'")

# if line[-8:] == "rejected":
#     print("The line ends with 'rejected'")



# QUICK CHECK: MODIFYING STRINGS What would be a quick way to change all
#  punctuation in a string to spaces? 

# #map all punctuation to spaces
# translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
# modified_string = x.translate(translator)



# TRY THIS: STRING OPERATIONS Suppose that you have a list of strings in which
#  some (but not necessarily all) of the strings begin and end with the double
#  quote character:
#  x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
#  What code would you use on each element to remove just the double quotes?
#  What code could you use to find the position of the last p in Mississippi?
#  When you’ve found that position, what code would you use to remove just
#  that letter? 

# x = [s.strip('"') for s in x]

# last_p_position = word.rfind('p')

# new_word = word[:last_p_position] + word[last_p_position+1:]



# QUICK CHECK: THE FORMAT() METHOD What will be in x when the following
#  snippets of code are executed?:
#  x = "{1:{0}}".format(3, 4)  # 4
#  x = "{0:$>5}".format(3) #$$$3
#  x = "{a:{b}}".format(a=1, b=5) # 1
#  x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10) # 1:$$$3



# QUICK CHECK: FORMATTING STRINGS WITH % What would be in the variable x
#  after the following snippets of code have executed?
#  x = "%.2f" % 1.1111 #1.11
#  x = "%(a).2f" % {'a':1.1111} #1.11
#  x = "%(a).08f" % {'a':1.1111} #1.11110000



# QUICK CHECK: BYTES For which of the following kinds of data would you want
#  to use a string? For which could you use bytes? 
# 1.Data file storing binary data
# #bytes.
# 2.Text in a language with accented characters
#  #string
# 3.Text with only uppercase and lowercase roman characters
# #string
# 4.A series of integers no larger than 255
# #bytes



#  LAB 6: PREPROCESSING TEXT In processing raw text, it’s quite often necessary
#  to clean and normalize the text before doing anything else. If you want to
#  find the frequency of words in text, for example, you can make the job easier
#  if, before you start counting, you make sure that everything is lowercase (or
#  uppercase, if you prefer) and that all punctuation has been removed. You can
#  also make things easier by breaking the text into a series of words. In this lab,
#  the task is to read the first part of the first chapter of Moby Dick (found in the
#  book's source code), make sure that everything is one case, remove all punc
# tuation, and write the words one per line to a second file. Because I haven’t
#  yet covered reading and writing files, here’s the code for those operations:


# with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
#     for line in infile:
#  # make all one case
#  line = line.lower()
#  # remove punctuation
#  line = line.translate(str.maketrans("", "", string.punctuation))
#  # split into words
#  words = line.split()
#  # write all words for line
#     for word in words:
#                 outfile.write(word + "\n")