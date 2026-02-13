class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        maxP = max(nums)
        currMax , currMin = 1,1
        
        for num in nums:
            if(num == 0):
                currMax , currMin = 1,1
            else:
                temp = currMax
                currMax = max(num*currMax , num*currMin , num)
                currMin = min(num*temp , num*currMin , num)
                maxP = max(maxP,currMax)

        return maxP