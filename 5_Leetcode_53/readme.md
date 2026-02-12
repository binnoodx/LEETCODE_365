## Leetcode 53 : Maximum Subarray

> Here is the complete solution for Leetcode Problem 238 called Maximum Subarray using Kadane Algorithm in Python. Also this Solution has optimized Time and Memory Complexity.

<a href="https://leetcode.com/problems/maximum-subarray/description/">Problem Link</a>


<a href="https://github.com/binnoodx/LEETCODE_365">Github Code</a>


<a href="https://www.youtube.com/watch?v=5WZl3MMT0Eg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=6">Reference Video</a>


---

## Question
<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770914877/1b478b97-0e91-4647-ae7f-271e6cd62361.png" />

---

## Question Detail

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770914891/dc140afb-2e10-46f0-a4b2-238ea8f6b1dc.png" />

---

## Solution Code

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """

        maxSum = nums[0] #since array of nums is Non - 0
        currSum = 0

        for num in nums:

            if(currSum < 0):
                currSum = 0
            
            currSum = currSum + num
            maxSum = max(maxSum , currSum)

        return maxSum
           
```

---



## Explanation of Solution

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770914902/WhatsApp_Image_2026-02-12_at_10.29.30_PM_vk1tbn.jpg" />
