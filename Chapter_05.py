# What would len() return for each of the following:
#  [0]; []; [[1, 3, [4, 5], 6], 7]? 1,0,2 



#  TRY THIS: LIST SLICES AND INDEXES Using what you know about the len()
#  function and list slices, how would you combine the two to get the second half
#  of a list when you don’t know what size it is? Experiment in the Python shell
#  to confirm that your solution works.
# list = [1, 2, 3, 4, 5, 6]
# mid = len(list) // 2
# second_half = list[mid:]



# TRY THIS: MODIFYING LISTS Suppose that you have a list 10 items long. How
#  might you move the last three items from the end of the list to the beginning,
#  keeping them in the same order?
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# last_three = my_list[-3:]
# rest_of_list = my_list[:-3]
# modified_list = last_three + rest_of_list
# print("Modified list:", modified_list)



# TRY THIS: SORTING LISTS Suppose that you have a list in which each element is
#  in turn a list: [[1, 2, 3], [2, 1, 3], [4, 0, 1]]. If you wanted to sort
#  this list by the second element in each list so that the result would be [[4,
#  0, 1], [2, 1, 3], [1, 2, 3]], what function would you write to pass as
#  the key value to the sort() method?
#  my_list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
# sorted_list = sorted(my_list, key=lambda x: x[1])



# QUICK CHECK: LIST OPERATIONS What would be the result of len([[1,2]] * 3)? 
# What are two differences between using the in operator and a list’s index()
#  method?
#  Which of the following will raise an exception?: min(["a", "b”, "c"]);
#  max([1, 2, "three"]); [1, 2, 3].count("one")

# my_list = [1, 2, 3]
# print(4 in my_list)       # False
# print(my_list.index(4))  # Raises ValueError



#  TRY THIS: LIST OPERATIONS If you have a list x, write the code to safely remove
#  an item if—and only if—that value is in the list.
#  Modify that code to remove the element only if the item occurs in the list
#  more than once.

# x = [1, 2, 3, 3, 4, 5]
# item = 3
# # Remove the item only if it occurs more than once
# if x.count(item) > 1:
#     x.remove(item)  # Removes the first occurrence of the item
# print(x)



# TRY THIS: LIST COPIES Suppose that you have the following list: x = [[1, 2,
#  3], [4, 5, 6], [7, 8, 9]] What code could you use to get a copy y of
#  that list in which you could change the elements without the side effect of
#  changing the contents of x? 

# import copy
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# y = copy.deepcopy(x)



# QUICK CHECK: TUPLES Explain why the following operations aren’t legal for
#  the tuple x = (1, 2, 3, 4):
#  x.append(1)
#  x[1] = "hello"
#  del x[2]
#  If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?

# x = (3, 1, 4, 2)
# sorted_x = tuple(sorted(x))



#  QUICK CHECK: SETS If you were to construct a set from the following list, how
#  many elements would the set have?: [1, 2, 5, 1, 0, 2, 3, 1, 1, (1,
#  2, 3)]

# unique_set = set([1, 2, 5, 1, 0, 2, 3, 1, 1, (1, 2, 3)])
# print(len(unique_set))  # Output: 6



#  LAB 5: EXAMINING A LIST In this lab, the task is to read a set of temperature
#  data (the monthly high temperatures at Heathrow Airport for 1948 through
#  2016) from a file and then find some basic information: the highest and low
# est temperatures, the mean (average) temperature, and the median tempera
# ture (the temperature in the middle if all the temperatures are sorted). 
# The temperature data is in the file lab_05.txt in the source code directory for
#  this chapter. Because I haven’t yet discussed reading files, here’s the code to
#  read the files into a list:
#  temperatures = []
#  with open('lab_05.txt') as infile:
#      for row in infile:
#         temperatures.append(int(row.strip())
#  You should find the highest and lowest temperature, the average, and the
#  median. You’ll probably want to use the min(), max(), sum(), len(),
#  and sort() functions/methods.

# temperatures = []
# with open('lab_05.txt') as infile:
#     for row in infile:
#         temperatures.append(int(row.strip()))  # Strip any extra whitespace and convert to int

# #highest and lowest temperatures
# highest_temp = max(temperatures)
# lowest_temp = min(temperatures)

# #mean temperature
# mean_temp = sum(temperatures) / len(temperatures)

# #median temperature
# temperatures.sort()  # Sort the list of temperatures
# n = len(temperatures)

# #number of temperatures is odd, the median is the middle value
# if n % 2 == 1:
#     median_temp = temperatures[n // 2]
# else:
#     #the median is the average of the two middle values
#     median_temp = (temperatures[n // 2 - 1] + temperatures[n // 2]) / 2