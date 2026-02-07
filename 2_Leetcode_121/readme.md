# Leetcode 121 : Best Time to Buy and Sell Stock

<a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/">Problem Link</a>


<a href="https://github.com/binnoodx/LEETCODE_365">Github Code</a>


<a href="https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=2">Reference Video</a>




## Problem
<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770454837/8193ddd6-907c-4b6d-93a9-4bf7ef8bba73.png" />



## Example

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770454962/be9a07cd-bfd7-4068-896f-425c92580f1f.png" />


## Solution Code
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0,1
        maxProfit = 0
        while(r<len(prices)):
            if(prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r 
            
            r+=1
        return maxProfit


```




## Explaination

<img src="https://res.cloudinary.com/dfda8kpnc/image/upload/v1770455057/WhatsApp_Image_2026-02-07_at_2.32.15_PM_gmr1kx.jpg" />

