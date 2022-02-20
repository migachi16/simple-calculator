import os
import re
import hashlib as hs
import numpy as np
import scipy as sp


left_par_idx = []       # Lists of parenthesis indices
right_par_idx = []
nums = []       # A list of all the numbers in the expression
operators = ''      # A string of all the operators in the expression
curr_dir = os.getcwd()
pass_addy = curr_dir + '\pass_hashes.txt'
user_data = (open(pass_addy, 'r')).read()


def check_parentheses(x: str) -> bool:
    """ Takes the expression as input. Checks whether parentheses 
    match correctly. If so, parse the expression into numbers and 
    the operators between them
    """
    global nums, operators, left_par_idx, right_par_idx
    left = 0
    right = 0

    for char in x:
        if right > left:
            return False
        if char == '(':
            left += 1
        elif char == ')':
            right += 1
    if left != right:
        return False

    # All is good -- we may proceed to populate the necessary lists.
    a = re.split('\(|\)|\*|\^|-|\+|\u00f7', x)
    b = re.split('[0-9, .]', x)

    nums = list(filter(None, a))
    for num in nums:
        if num.count('.') > 1:  # Taking care of multiple decimals
            return False

    operators = ''.join(b)
    for idx, op in enumerate(operators):
        if op == '(':
            left_par_idx.append(idx)
        if op == ')':
            right_par_idx.append(idx)

    return True


def execute(start_pos: int, end_pos: int) -> float:
    """ Recursive evaluation of basic calculation blocks, 
    sans parentheses. Called only by 'unifier' 
    """
    block_nums = list(map(float, nums[start_pos : end_pos]))   
    block_ops = operators[start_pos : end_pos - 1]      # New nums/ops lists
    zero = False        # Division by zero check

    total = block_nums[0]
    for i in range(1, len(block_nums)):
        next = block_nums[i]
        op = block_ops[i - 1]

        match op:
            case '-':
                if i + 1 == len(block_nums) or block_ops[i] in {'-', '+'}:
                    total -= next
                else:
                    total -= execute(i, end_pos)
                    break

            case '+':
                if i + 1 == len(block_nums) or block_ops[i] in {'-', '+'}:
                    total += next
                else:
                    total += execute(i, end_pos)
                    break

            case '*':
                if i + 1 == len(block_nums) or block_ops[i] != '^':
                    total *= next
                else:
                    total *= execute(i, end_pos)
                    break

            case '\u00f7':
                if i + 1 == len(block_nums) or block_ops[i] != '^':
                    try: 
                        total /= next
                    except(ZeroDivisionError):
                        zero = True
                        break
                else:
                    total /= execute(i, end_pos)
                    break

            case '^':
                total = total ** next

    if zero:
        total = None
    return total


def unifier(x: str) -> float:
    """ Breaks up the expression into parenthetical segments 
    and evaluates them, bottom up. """
    print(left_par_idx)
    print(right_par_idx)
    print(operators)
    print(nums)
    if len(nums) == 1:
        return nums[0]
    if not len(left_par_idx):
        return execute(0, len(nums))
    total = 0.0
    return 0.0


def history_list(history):
    """ Converts and reformats the history dictionary of previous calculations
    into a more readable format for the Show Log popup"""
    hist = str(history)
    hist = hist.replace('\'', '').replace('{', '').replace('}', '')
    hist = hist.replace(',', '\n').replace(':', ' = \n\t')
    return hist


def hashed(pw: str) -> str:
    masked = hs.sha256(pw.encode())
    return masked.hexdigest()
    

def login(id: str, pw: str) -> bool:
    a = ('', None)
    if id in a or pw in a or id == 'USERNAME':
        return False
    data_list = user_data.split(';')
    for datum in data_list:
        entry = datum.replace('\n', '').split(',')
        if id != entry[0]:
            continue
        else:
            temp = hashed(pw)
            if temp == entry[2]:
                return True
            break
    return False


def register(id: str, pw: str, email: str) -> str:
    A = ('', None)
    if id in A or pw in A or email in A or id == 'USERNAME':
        return 'Invalid'

    if ',' in id:
        return ','

    if '@' not in email or '.' not in email:
        return '@'

    data_list = user_data.split(';')
    for datum in data_list:
        entry = datum.replace('\n', '').split(',')
        if id != entry[0]:
            continue
        else:
            return 'IDExist'
    
    pw_hash = hashed(pw)
    new_entry = open(pass_addy, 'a')
    new_entry.write(id + ',\n' + email + ',\n' + pw_hash + '\n;')
    new_entry.close()
    return 'Success'
        

if __name__ == '__main__':
    #st = '(12.1*623^23)\u00f72-33+1'   # Should be evaluated to ~1.1349597 * 10^65
    #sta = '12.1*623^23\u00f72-33+1'
    #check_parentheses(sta)
    #d = {'12341*9': '111069.0', '111069.0*9': '999621.0', '999621.0÷8': '124952.625',
    #    '124952.625-645': '124307.625'}
    #print(history_list(d))

    #sta correctly evaluates to 1.1349597 * 10^65  ||||  2/19/22

    #a = ')(121)(' # False
    #b = '()()()9()' # True
    #c = '(1(12(3)*3)+21(23*2))' # True
    #d = '()(12))(' # False
    #print(check_parentheses(a))
    #print(check_parentheses(b))
    #print(check_parentheses(c))
    #print(check_parentheses(d))

    login('p', 'p')

    #print(hashed('aaaka'))
    #print(hashed('taaka'))
    #print(hashed('aaaka'))