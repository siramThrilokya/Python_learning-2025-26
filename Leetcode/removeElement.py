# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
       
nums = [3,2,2,3]
val = int(3)
for i in nums:
    if i == val:
        nums.remove(i)
        
print(nums)