class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        l = 0
        current_sum = 0
        max_sum = 0

        for r in range(len(nums)):
            current_sum += nums[r]
            freq[nums[r]] += 1

            if r - l + 1 > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                current_sum -= nums[l]
                l += 1

            if r - l + 1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
