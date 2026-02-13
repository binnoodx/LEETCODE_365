## Leetcode 152 : Maximum Product Subarray

> Here is the complete solution for Leetcode Problem 152 called Maximum Product Subarray in Python. Also this Solution has optimized Time and Memory Complexity.

<a href="https://leetcode.com/problems/maximum-product-subarray//">Problem Link</a>


<a href="https://github.com/binnoodx/LEETCODE_365">Github Code</a>


<a href="https://www.youtube.com/watch?v=lXVy6YWFcRM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=6">Reference Video</a>


---

## Question
<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770991926/d77babcc-afdc-4298-98fd-7c6b6e44a01e.png" />

---

## Question Detail

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770991929/a48a7140-05f4-4bb0-bd05-9e38060e9c09.png" />

---

## Solution Code

```python
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
```

---



## Explanation of Solution

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770992720/WhatsApp_Image_2026-02-13_at_7.52.24_PM_l9tv7p.jpg" />
