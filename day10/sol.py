class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        t=[0]*N
        td=[0]*N
        for i in trust:
            t[-1+i[0]]=1
            td[-1+i[1]]+=1
        for i in range(0,N):
            if t[i] == 0 and td[i] == N-1:
                return i+1
        return -1
