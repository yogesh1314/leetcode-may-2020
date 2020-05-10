class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #Take 3
        a=1
        while(num>0):
            num=num-a
            a=a+2
        return num==0
        #Take 2
        if(num <=2):
            return True
        s=1
        e=num
        while s<=e:
            m=int(s+(e-s)/2)
            print(m)
            if(m*m == num):
                return True
            if(m*m < num):
                s=m+1
            else: e=m-1
        return False
        # Take 1
        return 0==sqrt(num)-floor(sqrt(num))
