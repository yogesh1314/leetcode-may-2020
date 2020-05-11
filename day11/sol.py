class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        r=len(image)
        c=len(image[0])
        a=[]
        trav=[]
        a.append([sr,sc])
        oc=image[sr][sc]
        while len(a)>0:
            ele=a.pop()
            i=ele[0]
            j=ele[1]
            if oc==image[i][j]:
                image[i][j]=newColor
                if (i-1>=0 and i-1<=r-1) and (j>=0 and j<=c-1) and not ([i-1,j] in trav):
                    a.append([i-1,j])
                    trav.append([i-1,j])
                if (i+1>=0 and i+1<=r-1) and (j>=0 and j<=c-1) and not ([i+1,j] in trav):
                    a.append([i+1,j])
                    trav.append([i+1,j])
                if (i>=0 and i<=r-1) and (j+1>=0 and j+1<=c-1) and not ([i,j+1] in trav):
                    a.append([i,j+1])
                    trav.append([i,j+1])
                if (i>=0 and i<=r-1) and (j-1>=0 and j-1<=c-1) and not ([i,j-1] in trav):
                    a.append([i,j-1])
                    trav.append([i,j-1])
        return image
