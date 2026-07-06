class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allm=1
        allz=1
        pz=[]

        for i in range(len(nums)):
            if nums[i] == 0:
                pz.append(i)
            else:
                allm=allm*nums[i]
        res=[0]*len(nums)

        if len(pz)>1:
            return res
        elif len(pz)==1:
            c = pz[0]
            res[c]=allm
            return res
        else:
            return [allm//e for e in nums]
            