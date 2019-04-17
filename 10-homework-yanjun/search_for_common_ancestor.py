'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        minn = min(p.val, q.val)
        maxn = max(p.val, q.val)
        if root is None:
            return None
        if minn <= root.val <= maxn:
            return root
        else:
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)
            if l:
                return l
            if r:
                return r


a = Tree = TreeNode(6)
b = Tree.left = TreeNode(2)
c = Tree.right = TreeNode(8)
d = b.left = TreeNode(0)
e = b.right = TreeNode(4)
f = c.left = TreeNode(7)
e = c.right = TreeNode(9)
f = e.right = TreeNode(3)
g = e.right = TreeNode(5)
s = Solution()
print(s.lowestCommonAncestor(a, b, c).val)