class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sum1 = sum(nums)
        target=sum1%p
        if target==0:
            return 0
        n=len(nums)
        prefix=0
        ans=n
        mp={0: -1}
        for i in range(n):
            prefix=(prefix + nums[i]) % p
            need=(prefix - target) % p
            if need in mp:
                ans=min(ans, i - mp[need])
            mp[prefix]=i
        if ans<n:
            return ans 
        else:
            return -1
