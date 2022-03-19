# Time complexity: O(n)
def reverse(x: int) -> int:
    num = abs(x)
    res = 0
    while num:
        res = res*10 + num % 10
        num //= 10

    return res if x > 0 else -res
