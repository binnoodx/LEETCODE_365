# Leetcode 121 : Best Time to Buy and Sell Stock

<a href="https://leetcode.com/problems/product-of-array-except-self/">Problem Link</a>


<a href="https://github.com/binnoodx/LEETCODE_365">Github Code</a>


<a href="https://www.youtube.com/watch?v=bNvIQI2wAjk&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=4">Reference Video</a>




## Problem
<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770733069/61b089fb-a6ca-42cc-b8a8-4b37b6710ae5.png" />



## Example

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770733075/e2afe35e-3641-4a2e-927f-fd0a12f9968e.png" />


## Solution Code
```python
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
```




## Explaination

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770733154/WhatsApp_Image_2026-02-10_at_8.03.54_PM_bvab59.jpg" />

