class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_dict = {}
        for n in nums:
            if n in nums_dict:
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1
        for k in nums_dict.keys():
            if nums_dict[k] % 2 != 0:
                return False
        return True
