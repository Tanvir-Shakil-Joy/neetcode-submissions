class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major = nums[0]
        for num in nums:
            if count == 0:
                count += 1
                major = num
            else:
                if num == major:
                    count += 1
                else:
                    count -= 1
        return major