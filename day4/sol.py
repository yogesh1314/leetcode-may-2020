class Solution:
    def findComplement(self, num: int) -> int:
        # Take 1
        return num^-1+2**len(bin(num)[2:])
        # Take 2
        nb=(int)(math.floor(math.log(num)/math.log(2))) + 1
        return ((1<<nb)-1)^num
