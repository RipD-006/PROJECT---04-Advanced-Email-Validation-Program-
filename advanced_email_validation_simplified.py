# [PYTHON PROGRAM] : Email ID Validation using Regex Module

# Conditions of a Valid Email ID :
# a - z
# 0 - 9
# "." "@" and "_" should occur only once.
# "." should occur only at index position [2] or [3] before the ending.

import re       # Importing the "REGEX" module.
email_condition = "^[a - z] + [\._] ? [a - z 0 - 9] + [@]\w + [.]\w {2 , 3} $"
# "^" denotes "startswith" in REGEX;
# "\" is used to search a character through REGEX;
# "?" returns either 0 ["False"] or 1 ["True"] in REGEX;
# "\w" is used to search a special character through REGEX;
# "{}" is used to find a specific character in a particular position through REGEX;
# "$" is used to find a specific character from right-to-left [i.e Negative Indexing] of the string in REGEX;

user_email = input("Enter Email ID: ")

# The "search" function within REGEX module will compare the user entered email [i.e "user_email"] with the conditions set for a valid Email ID [i.e "email_condition"].
if re.search(email_condition , user_email):     # Conditional "if-else" to check wheather the user entered email is valid or invalid. 
    print("Valid Email.")
else:
    print("Invalid Email.")