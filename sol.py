class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=len(coordinates)
        if n==2:
            return True
        for i in range(1,n-3):
            x1=coordinates[i][0];
            x2=coordinates[i+1][0];
            x3=coordinates[i+2][0];
            y1=coordinates[i][1];
            y2=coordinates[i+1][1];
            y3=coordinates[i+2][1];
            prd=((x2-x1)*(y3-y1))-((y2-y1)*(x3-x1))
            if prd!=0:
                return False
        return True
