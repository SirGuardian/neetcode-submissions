class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            index1 = i
            for y in range(i+1, len(nums),1):
                index2 = y
                if nums[i] + nums[y] == target:
                    list = [index1, index2]
                    return list

            