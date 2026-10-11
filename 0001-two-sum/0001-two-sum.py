class Solution(object):
    def twoSum(self, nums, target):
        s={}
        for i,n in enumerate(nums) :
            if target-n in s :
                return [s[target-n],i]
            else :
                s[n]=i
        