# Time complexity: O(n)
# Space complexity: O(1)
def is_number_palindrome(x: int) -> bool:
    num = str(x)
    l, r = 0, len(num) - 1

    while l < r:
        if num[l] != num[r]:
            return False

        l += 1
        r -= 1

    return True
