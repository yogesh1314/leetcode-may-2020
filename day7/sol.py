# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root==None:
            return False
        tmp=TreeNode(-1)
        q=[]
        q.append((root,tmp))
        parX = None
        parY = None
        while len(q)>0:
            lenQ=len(q)
            while lenQ:
                ele=q.pop(0)
                if ele[0].val ==x:
                    parX=ele[1]
                if ele[0].val ==y:
                    parY=ele[1]
                if ele[0].left:
                    q.append((ele[0].left,ele[0]))
                if ele[0].right:
                    q.append((ele[0].right,ele[0]))
                lenQ-=1
                if parX and parY:
                    break
            if parX and parY:
                return parX != parY
            if (parX and not parY) or (parY and not parX):
                return False
        return False
        
