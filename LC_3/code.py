class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_s=""
        l=[]
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        n = len(s)
        begin=0
        current=1
        temp_s+=s[begin]
        while begin<current and current < n:
            if s[current] in temp_s:
                l.append(temp_s)
                temp_s=""
                begin+=1
                current=begin+1
                temp_s+=s[begin]
            else:
                temp_s+=s[current]
                current+=1
        l.append(temp_s)
        return len(max(l, key=len))
        
