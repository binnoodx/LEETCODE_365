class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newList = set()
        for num in nums:
            if num in newList:
                return True
            else:
                newList.add(num)
        return False
        