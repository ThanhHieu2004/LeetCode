# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     next_num = target - nums[i]
        #     if next_num in nums[i+1:]:
        #         i_2 = nums.index(next_num, i+1,)
        #         return [i, i_2]
        # return []
        nums_dict = {}
        result = []
        for i, num in enumerate(nums):
            nums_dict[num] = i
            subtracted_value = target-num
            if subtracted_value in nums_dict:
                if i != nums_dict[subtracted_value]:
                    return [nums_dict[target-num], i]
                elif i == nums_dict[subtracted_value]:
                    result.append(i)
                    continue
        return result
        
        

        