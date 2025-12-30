class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        j =  list(heapq.merge(nums1, nums2))
        # j.sort()
        if (len(j) % 2 == 0):
            index = len(j) // 2 
            # return (j[index] + j[index - 1])
            return (j[index] + j[index -1 ]) / 2
            pass
        else:
            return  j[(len(j) // 2)]

        # print(j)

        return 0