class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        for x in range(left , right+1):
            found = False
            for start, end in ranges:
                if start<= x <= end:
                    found = True
                    break
            if found == False : return False
        return True 