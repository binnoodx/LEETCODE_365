# Leetcode 121 : Best Time to Buy and Sell Stock

<a href="https://leetcode.com/problems/contains-duplicate/description/">Problem Link</a>


<a href="https://github.com/binnoodx/LEETCODE_365">Github Code</a>


<a href="https://www.youtube.com/watch?v=3OamzN90kPg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=3">Reference Video</a>




## Problem
<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770649032/6152c54b-5923-4cd4-a57b-db509ef560e2.png" />



## Example

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770649068/c366e4a4-7bf7-4173-85b9-096494646616.png" />


## Solution Code
```python
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
        


```




## Explaination

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770649007/WhatsApp_Image_2026-02-09_at_8.37.10_PM_zhcywn.jpg" />

