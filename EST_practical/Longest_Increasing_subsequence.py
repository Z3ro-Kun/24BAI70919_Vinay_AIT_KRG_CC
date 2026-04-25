class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        arr=[]
        for i in nums:
            idx=bisect.bisect_left(arr, i)
            if idx==len(arr):
                arr.append(i)
            else:
                arr[idx]=i
        return len(arr)
