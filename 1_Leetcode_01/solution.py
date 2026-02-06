

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {} 

        for index, num  in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff] , index]
            hashMap[num] = index
        return
        

        