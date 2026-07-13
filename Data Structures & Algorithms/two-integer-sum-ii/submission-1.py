class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ln=len(numbers)

        l,r=0,ln-1

        while l<r:
            val=numbers[l]+numbers[r]
            if val == target:
                return [l+1,r+1]
            elif val>target:
                r-=1
            else:
                l+=1
        return []
            