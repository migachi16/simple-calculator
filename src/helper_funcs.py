import os
import re
import hashlib as hs
import numpy as np
import scipy as sp
import math


left_par_idx = []       # Lists of parenthesis indices
right_par_idx = []
nums = []               # A list of all the numbers in the expression
operators = ''          # A string of all the operators in the expression

curr_dir = os.getcwd()  # Current directory

# Find and read user login ID's and password hashes
pass_addy = os.path.dirname(curr_dir) + '/pass_hashes.txt'  
user_data = (open(pass_addy, 'r')).read()

# Empty data reference
A = ('', None)

def evaluate(expression: list) -> float:
    try:
        one = ''.join(expression)
        answer = eval(one)
        return float(answer)
    except(TypeError):
        return '!!!'
    except(ZeroDivisionError):
        return None
    except(ValueError):
        return '???'

def history_list(history):
    """ Converts and reformats the history dictionary of previous calculations
    into a more readable format for the Show Log popup"""
    hist = str(history)
    hist = hist.replace('\'', '').replace('{', '').replace('}', '')
    hist = hist.replace(',', '\n').replace(':', ' = \n\t')
    return hist


def hashed(pw: str) -> str:
    """ Return the sha256 hashed value of the password """

    masked = hs.sha256(pw.encode())
    return masked.hexdigest()


def login(id: str, pw: str) -> bool:
    """ Check to see if the user passed valid login information"""

    if id in A or pw in A or id == 'USERNAME':
        return False
    # Parse through user data
    data_list = user_data.split(';')
    for datum in data_list:
        entry = datum.replace('\n', '').split(',')
        # Find a matching login ID
        if id != entry[0]:
            continue
        else:
            # Check for matching password hash 
            temp = hashed(pw)
            if temp == entry[2]:
                return True
            break
    return False


def register(id: str, pw: str, email: str) -> str:
    """ Register the user for an AMSC account"""

    if id in A or pw in A or email in A or id == 'USERNAME':
        return 'Invalid'

    if ',' in id:
        return ','

    if '@' not in email or '.' not in email:
        return '@'

    data_list = user_data.split(';')
    for datum in data_list:
        entry = datum.replace('\n', '').split(',')
        # Check for existing login ID
        if id != entry[0]:
            continue
        else:
            return 'IDExist'
    
    pw_hash = hashed(pw)
    new_entry = open(pass_addy, 'a')
    new_entry.write(id + ',\n' + email + ',\n' + pw_hash + '\n; \n')
    new_entry.close()
    return 'Success'
        

if __name__ == '__main__':
    #st = '(12.1*623^23)\u00f72-33+1'   # Should be evaluated to ~1.1349597 * 10^65
    #sta = '12.1*623^23\u00f72-33+1'
    #st = '(2+80)*(3**(74-79))'
    #st = '2 + 5'
    #check_parentheses(sta)
    #d = {'12341*9': '111069.0', '111069.0*9': '999621.0', '999621.0÷8': '124952.625',
    #    '124952.625-645': '124307.625'}
    #print(history_list(d))

    #sta correctly evaluates to 1.1349597 * 10^65  ||||  2/19/22

    #a = ')(121)(' # False
    #b = '()()()9()' # True
    #c = '(1*(12*(3)*3)+21*(23*2))' # True
    #d = '()(12))(' # False
    #print(check_parentheses(a))
    #print(check_parentheses(b))
    #print(check_parentheses(c))
    #print(check_parentheses(d))

    #e = 'math.sin(math.e / 2)'

    #login('p', 'p')

    #print(hashed('aaaka'))
    #print(hashed('taaka'))
    #print(hashed('aaaka'))

    #b = unifier(st)

    #print(eval(e))

    pass