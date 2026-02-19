from collections import defaultdict
from typing import List

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = defaultdict(int)

        for day in responses:
            unique_responses = set(day)
            for word in unique_responses:
                freq[word] += 1

        max_freq = 0
        result = ""

        for word, count in freq.items():
            if count > max_freq or (count == max_freq and word < result):
                max_freq = count
                result = word

        return result
