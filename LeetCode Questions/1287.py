from collections import Counter

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def find_special_integer(arr):
            count = Counter(arr)
            max_count = max(count.values())
            for key, value in count.items():
                if value == max_count and value > len(arr) * 0.25:
                    return key

        return find_special_integer(arr)
