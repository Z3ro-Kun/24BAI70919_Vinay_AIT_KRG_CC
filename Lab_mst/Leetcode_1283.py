class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        import math
        while left<right:
            mid=(left+right)//2
            total=0
            for n in nums:
                total+=math.ceil(n/mid)
            if total<=threshold:
                right=mid
            else:
                left=mid+1
        return left
