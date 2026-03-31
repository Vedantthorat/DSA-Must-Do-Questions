class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = suffix = 1
        ans = [1] * n
        for i in range(n):

            ans[i] = prefix
            prefix *= nums[i]

        for i in range(n-1, -1, -1):

            ans[i] *= suffix
            suffix *= nums[i]

        return ans

  '''


  Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 '''
