class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rlist = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            rlist[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            rlist[i] = rlist[i] * postfix
            postfix = postfix * nums[i]
        return rlist

        