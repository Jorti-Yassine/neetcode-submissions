class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,e in enumerate(nums): 
            if e > 0:
                break
            if i>0 and e == nums[i-1]:
                continue

            l,r=i+1,len(nums)-1
            while l<r:
                tmp=nums[r]+nums[l]+e
                if tmp==0:
                    res.append([nums[l],e,nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif tmp<0:
                    l+=1
                else:
                    r-=1

        return res

            

