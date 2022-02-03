import decimal
import re

def typed_out(x: str) -> int:
    pass

def execute(x: str) -> float:
    """
    Input parsing and expression execution
    """
    nums = list(filter(None, (re.split('\(|\)|\*|\^|-|\+|\u00f7', x)))) # A list of all the numbers in the expression
    operators = ''.join(re.split('[0-9, .]', x)) # A list of all the operators in the expression
    print(operators)
    print(nums)
    total = 0.0
    for op in operators:
        match op:
            case '(':
                continue
            case ')':
                continue
            case '-':
                continue
            case '+':
                continue
            case '*':
                continue
            case '\u00f7':
                continue
            case '^':
                continue
    return total

def check_parentheses(x: str) -> bool:
    #
    # Check whether parentheses match in order
    #
    valid = True
    left = 0
    right = 0
    for char in x:
        if char == '(':
            left += 1
        elif char == ')':
            right += 1
        if right > left: # An expression is invalid if this is true at any point in the loop
            valid = False
            break
    if left != right: # Final check
        valid = False
    return valid

#
# Tests
#

sta = '(12.1*623^23)\u00f72-33+1' # Should be evaluated to ~1.1349597 * 10^65
execute(sta)

#a = ')(121)(' # False
#b = '()()()9()' # True
#c = '(1(12(3)*3)+21(23*2))' # True
#d = '()(12))(' # False
#print(check_parentheses(a))
#print(check_parentheses(b))
#print(check_parentheses(c))
#print(check_parentheses(d))
