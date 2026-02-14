## Leetcode 153 : Find Minimum in Rotated Sorted Array

> Here is the complete solution for Leetcode Problem 153 called Find Minimum in Rotated Sorted Array using Binary Search in Python. Also this Solution has optimized Time and Memory Complexity.

<a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/">Problem Link</a>


<a href="https://github.com/binnoodx/LEETCODE_365">Github Code</a>


<a href="https://www.youtube.com/watch?v=lXVy6YWFcRM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=7">Reference Video</a>


---

## Question
<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1771085470/93c442a3-5a05-4deb-b52f-5a8d3366d61c.png" />

---

## Question Detail

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1771085472/70fd28c7-9ca6-4d16-8256-c3a8bccb7dc9.png" />

---

## Solution Code

```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums [0]
        left , right = 0 , len(nums)-1 #Index

        while left<=right:

            if(nums[left]<nums[right]):
                res = min(res , nums[left])
                break
            
            mid = (left + right) // 2
            res = min(nums[mid] , res)

            if(nums[left] <= nums[mid] ):
                left = mid +1
            else:
                right = mid-1
        return res      
```

---



## Explanation of Solution

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1771088354/WhatsApp_Image_2026-02-14_at_9.54.35_PM_hty6xw.jpg" />
<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1771085481/2_j37q8r.jpg" />

