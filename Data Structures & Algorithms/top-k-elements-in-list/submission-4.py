class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = list(dict(sorted(Counter(nums).items(), key=lambda item: item[1])))

        return res[len(res)-k:]