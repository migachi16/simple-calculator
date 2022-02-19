import re
import numpy as np
import scipy as sp

left_par_idx = []       # Lists of parenthesis indices
right_par_idx = []
nums = []       # A list of all the numbers in the expression
operators = ''      # A string of all the operators in the expression

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
    """ Breaks up the expression into parenthetical segments and evaluates them, bottom up. """
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


def history_list(history: dict) -> str:
    """ Converts and reformats the history dictionary of previous calculations
    into a more readable format for the Show Log popup"""
    hist = str(history)



    return hist


if __name__ == '__main__':
    st = '(12.1*623^23)\u00f72-33+1'   # Should be evaluated to ~1.1349597 * 10^65
    sta = '12.1*623^23\u00f72-33+1'
    check_parentheses(sta)
    
    #sta correctly evaluates to 1.1349597 * 10^65  ||||  2/19/22

    #a = ')(121)(' # False
    #b = '()()()9()' # True
    #c = '(1(12(3)*3)+21(23*2))' # True
    #d = '()(12))(' # False
    #print(check_parentheses(a))
    #print(check_parentheses(b))
    #print(check_parentheses(c))
    #print(check_parentheses(d))
