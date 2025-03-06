# You are given an array of integers nums,
#  there is a sliding window of size k which
#  is moving from the very left of the array to
#  the very right. You can only see the k numbers 
# in the window. Each time the sliding window moves 
# right by one position.

# Return the max sliding window.


from collections import deque
import numpy as np
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        length = len(nums)
        d_num = deque(nums[i:i+k])
        output_array = []
        temp = max(d_num)
        output_array.append(temp)
        last_max = temp
        if(k==1):
            return nums
        for i in range(k,length):
            poped_elemnt = d_num.popleft()
            d_num.append(nums[i])
            if(last_max < nums[i]):
                output_array.append(nums[i])
                last_max = nums[i]
            else:
                if(poped_elemnt == last_max and last_max != d_num[0]):
                    haha = max(d_num)
                    output_array.append(haha)
                    last_max = haha
                else:
                    output_array.append(last_max)
        return output_array


