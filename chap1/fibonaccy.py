'''
Fibonacci problem
'''
import time
from typing import Dict
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}

def fib_rec(n: int) -> int:
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n-2)

def fib_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

@lru_cache(maxsize=None)
def fib_auto_memo(n: int) -> int:
    if n < 2:
        return n
    return fib_auto_memo(n - 2) + fib_auto_memo(n - 1)

def fib_iter(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

def calc_time(func, n):
    t_start = time.time()
    fib = func(n)
    t_delta = time.time() - t_start
    print('{func}({n}) = {fib}. Time spent: {t_delta}sec.'.format(func=func.__name__, n=n, fib=fib, t_delta=t_delta))


if __name__ == '__main__':
    calc_time(fib_rec, 30)
    calc_time(fib_memo, 30)
    calc_time(fib_auto_memo, 30)
    calc_time(fib_iter, 30)
