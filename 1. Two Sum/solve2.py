class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for i, num in enumerate(nums):
            tmp = target - num
            if tmp in hash_table:
                return i, hash_table[tmp]
            hash_table[num] = i
        return []
