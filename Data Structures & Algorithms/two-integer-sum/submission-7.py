class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                list = [hashmap[compliment], i]
                return list
            else:
                hashmap[nums[i]] = i