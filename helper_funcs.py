import decimal
import re

left_par_idx = []   # Lists of parenthesis indices
right_par_idx = []
nums = []   # A list of all the numbers in the expression
operators = ''  # A string of all the operators in the expression

def check_parentheses(x: str) -> bool:
    """
    Takes the expression as input. Checks whether parentheses match correctly. If so, parse the expression.
    """
    global nums, operators, left_par_idx, right_par_idx
    valid = True
    left = 0
    right = 0
    for char in x:
        if right > left:    # An expression is invalid if this is true at any point in the loop
            valid = False
            break
        if char == '(':
            left += 1
        elif char == ')':
            right += 1
    if left != right:
        return False
    #
    # All is good -- we may proceed to populate the necessary lists.
    #   
    a = re.split('\(|\)|\*|\^|-|\+|\u00f7', x)  # Regex helps!
    b = re.split('[0-9, .]', x)
    nums = list(filter(None, a))
    operators = ''.join(b)
    for idx, op in enumerate(operators):
        if op == '(':
            left_par_idx.append(idx)
        if op == ')':
            right_par_idx.append(idx)
    return True

def execute(start_pos: int, end_pos: int) -> float:
    """
    Evaluation of basic calculation blocks, sans parentheses. Called only by 'unifier'
    """
    block_nums = list(map(float, nums[start_pos : end_pos]))
    block_ops = operators[start_pos : end_pos - 1]
    total = block_nums[0]
    for i in range(1, len(block_nums)):
        next = block_nums[i]
        op = block_ops[i - 1]
        match op:
            case '-':
                continue
            case '+':
                if i + 1 == len(block_nums) or block_ops[i] != '^':
                    total += next
            case '*':
                continue
            case '\u00f7':
                continue
            case '^':
                continue
    return total

def unifier(x: str) -> float:
    """
    Breaks up the expression into parenthetical segments and evaluates them, bottom up.
    """
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

#
# Tests
#

st = '(12.1*623^23)\u00f72-33+1'   # Should be evaluated to ~1.1349597 * 10^65
sta = '12.1*623^23\u00f72-33+1'
check_parentheses(sta)

#a = ')(121)(' # False
#b = '()()()9()' # True
#c = '(1(12(3)*3)+21(23*2))' # True
#d = '()(12))(' # False
#print(check_parentheses(a))
#print(check_parentheses(b))
#print(check_parentheses(c))
#print(check_parentheses(d))
