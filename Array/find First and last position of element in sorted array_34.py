class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find_left():

            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:

                mid = (left + right ) // 2

                if nums[mid] == target:

                    ans = mid

                    right = mid - 1

                elif nums[mid] < target:

                    left = mid + 1

                else:

                    right = mid - 1

            return ans

        def find_right():
            
            ans = -1
            left, right = 0, len(nums) - 1

            while left <= right:

                mid = (left + right ) // 2

                if nums[mid] == target:

                    ans = mid

                    left = mid + 1

                elif nums[mid] < target:

                    left = mid + 1

                else:

                    right = mid - 1
            return ans

        return [find_left(), find_right()]

'''


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 '''
