class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Take 1
        map=[0]*26
        for i in s:
            map[ord(i)-97]+=1
        for i in range(0,len(s)):
            if 1==map[-97+ord(s[i])]:
                return i
        return -1
        # Take 2
        ss= set()
        for i,e in enumerate(s):
            if e in ss: continue
            else: ss.add(s[i])
            if e in s[i+1:]: continue
            else: return i
        return -1

        
