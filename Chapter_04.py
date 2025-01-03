
# TRY THIS: VARIABLES AND EXPRESSIONS

x = 3 - 2 * (9 % 3)
print(x)

y = 3 - (2 * 9) % 3
print(y)

z = (3 - 2) * 9 % 3
print(z)




# TRY THIS: MANIPULATING STRINGS AND NUMBERS

int0 = 5
float0 = 4.5
string0 = "string"
compelex0 = 3+4j

result0 = string0 * int0
print(result0) # Repeats the string

result1 = string0 * float0
print(result1) # Raises TypeError

result2 = string0 * compelex0
print(result2) # Raises TypeError


import math
# The math module works with integers and floats.
sqrt0 = math.sqrt(25)
print(sqrt0)


import cmath
# The cmath module supports complex numbers,integers and floats.For floats and integers, it returns in the complex domain
csqrt0 = cmath.sqrt(25)
print(csqrt0)

# If you want to make sure you're using the math module functions again after importing cmath,
# you can explicitly reference math when calling functions or re-import the math module to clarify your intent.




# TRY THIS: GETTING INPUT

user_input = input("Enter something: ")
print(f"You entered: {user_input}")

user_input = int(input("Enter an integer: "))
# You can use int() to cconvert user input to integer

user_input = float(input("Enter a float: "))
# You can use float() to convert user input to float

# How to handle wrong types error? try-except blocks:
try:
    user_input = int(input("Enter something: "))
    print(f"You entered: {user_input}")
except ValueError:
    print("Error: You must enter an integer!")




# QUICK_CHECK

# Which of the following variable and function names do you think are not good Pythonic style? Why? 

# bar(), varName, VERYLONGVARNAME, foobar, longvarname,
# foo_bar(), really_very_long_var_name



# varName : Uses camelCase, which is not standard for variable names in Python. Python prefers snake_case for variable and function names. (var_name)

# VERYLONGVARNAME: All-uppercase names are typically reserved for constants.

# foobar : Python prefers snake_case for variable and function names. (foo_bar)

# longvarname : (long_var_name)

# really_very_long_var_name : Acceptable but not ideal.