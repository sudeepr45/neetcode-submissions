
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = []

        for num in count:
            result.append(num)

        result.sort(key=lambda num: count[num], reverse=True)

        return result[:k]