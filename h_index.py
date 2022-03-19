# Time complexity: O(nlogn)
# Space complexity: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        i = 0
        while i < n:
            if citations[i] >= (n-i):
                return n-i
            i += 1
        return 0
