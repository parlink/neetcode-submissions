class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for index, number in enumerate(nums):
            needed = target - number
            if needed in numbers:
                return [numbers[needed], index]
            else:
                numbers[number] = index
        return []