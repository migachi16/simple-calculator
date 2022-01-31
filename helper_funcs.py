import decimal
import re

def typed_out(x: str) -> int:
    pass

def execute(x: str) -> float:
    nums = re.split('\*|\^|-|\+|\u00f7', x)
    operators = list(filter(('').__ne__, re.split('[0-9, .]', x)))
    total = 0

    return 0.0

#sta = '12.1*623^23\u00f70-33+1'
#ops = list(filter(('').__ne__, re.split('[0-9, .]', sta)))
#numz = re.split('\*|\^|-|\+|\u00f7', sta)
#print(ops)