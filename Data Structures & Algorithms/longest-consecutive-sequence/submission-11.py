class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        count=1
        s_nums=list(sorted(set(nums)))
        max_seq=1
        
        for i in range(1,len(s_nums)):
            if s_nums[i-1]==s_nums[i]-1:
                count+=1
            else:
                count=1
            max_seq=max(max_seq,count)
        return max_seq