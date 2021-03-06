# Time complexity: O(n)
# Space complexity: O(1)
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1

        elif A[equal] == pivot:
            equal += 1

        else:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]
