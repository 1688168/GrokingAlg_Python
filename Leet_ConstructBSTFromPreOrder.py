# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



class Solution:
    def __init__(self):
        self.root = None

    def bstFromPreorder(self, preorder):
        if len(preorder) <= 0:
            return self.root

        def findInsertPoint(v, root):
            if root is None:
                return None

            if v < root.val:
                if root.left is not None:
                    return findInsertPoint(v, root.left)
                else:
                    return root

            else:
                if root.right is not None:
                    return findInsertPoint(v, root.right)
                else:
                    return root

        def insert(v):
            if self.root is None:
                self.root = TreeNode(v)
                return
            itr = findInsertPoint(v, self.root)

            if v < itr.val:
                itr.left = TreeNode(v)
            else:
                itr.right = TreeNode(v)

        for v in preorder:
            print("inserting v: ", v)
            insert(v)

        return self.root

s=Solution()
s.bstFromPreorder([8,5,1,7,10,12])

