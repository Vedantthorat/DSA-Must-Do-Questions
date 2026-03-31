class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        new_list = sorted(set(nums))

        max_sequence = 1

        count = 1

        for i in range(1, len(new_list)):

            if new_list[i] == (new_list[i-1] + 1):
                count += 1

            else:

                count = 1

            max_sequence = max(max_sequence, count)

        return max_sequence

  '''

  Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3

 '''
