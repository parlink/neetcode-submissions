class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for j in range(0, len(nums)):
            if nums[j] in seen:
                return True
            else:
                seen.add(nums[j])
        return False
        