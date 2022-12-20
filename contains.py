class Solution:
    def containsDuplicate(self, nums):
        return not len(nums)==len(set(nums))

List=[1,2,3,1,2]
obj=Solution()
result=obj.containsDuplicate(List)
print(result)