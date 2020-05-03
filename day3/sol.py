class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ## Take 1 
        mr=[0]*26;
        mm=[0]*26;
        for i in ransomNote:
            mr[ord(i)-97]+=1
        for i in magazine:
            mm[ord(i)-97]+=1
        for i in range(0,len(mr)):
            if(mr[i]>0):
                if(mr[i]>mm[i]):
                    print ("false")
                    return 0
        return 1

        #Take 2
        return not len(Counter(ransomNote) - Counter(magazine))
        #Take 3 
        return all(ransomNote.count(r) <= magazine.count(r) for r in set(ransomNote))
