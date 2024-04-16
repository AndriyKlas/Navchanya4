from collections.abc import Iterable
from typing import Union
import math

def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[ int , float ] , str] :
    d=b*b-4*a*c
    if d>0:
        d=math.sqrt(d)
        x1=(-b+d)/(2*a)
        x2=(-b-d)/(2*a)
        return [x1 ,x2]
    elif d==0:
        x = -b / (2 * a)
        return [x , x]
    elif d<0:
        return ["No real roots"]



# These "asserts" are used for self-checking
assert list(quadratic_roots(1, 0, -1)) == [1, -1]
assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]
assert list(quadratic_roots(1, 4, 4)) == [-2, -2]
assert list(quadratic_roots(1, -5, 6)) == [3, 2]
assert list(quadratic_roots(1, -6, 9)) == [3, 3]
assert list(quadratic_roots(2, 2, 1)) == ["No real roots"]
assert list(quadratic_roots(2, -7, 6)) == [2, 1.5]
assert list(quadratic_roots(2, -3, 1)) == [1, 0.5]

print("The mission is done! Click 'Check Solution' to earn rewards!")
