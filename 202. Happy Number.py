# solution 1. Detect cycles with HashSet
def isHappy(n: int) -> bool:
    def get_next(n):
        sums = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sums += digit ** 2
        return sums

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

# solution 2: Floyd's Cycle-Finding Algorithm
# if n is a happy number, i.e. there is no cycle,
# then the fast runner will eventually get to 1 before
# the slow runner
# if n is not a happy number, then eventually the fast
# runner and the slow runner will be on the same number.
def isHappy(n: int) -> bool:
    def get_next(number):
        sums = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sums += digit ** 2
        return sums
    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1


