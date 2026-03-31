class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curr_sum = 0
        count = 0
        dict1 = {0: 1}

        for num in nums:

            curr_sum += num

            if curr_sum - k in dict1:

                count += dict1[curr_sum - k]

            dict1[curr_sum] = dict1.get(curr_sum,0) +1

        return count

'''

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

'''
