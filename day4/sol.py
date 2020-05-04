class Solution:
    def findComplement(self, num: int) -> int:
        nb=(int)(math.floor(math.log(num)/math.log(2))) + 1
        return ((1<<nb)-1)^num
