#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (45.52%)
# Total Accepted:    27.1K
# Total Submissions: 59.2K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    #     if root == None:
    #         return True
    #     return self.checkTwoTree(root.left,root.right)
    # def checkTwoTree(self,leftTree,rightTree):
    #     if leftTree==None and rightTree==None:
    #         return True
    #     if leftTree!=None and rightTree==None:
    #         return False
    #     if leftTree==None and rightTree!=None:
    #         return False
    #     if leftTree.val != rightTree.val:
    #         return False
    #     left = self.checkTwoTree(leftTree.left,rightTree.right)
    #     right = self.checkTwoTree(leftTree.right,rightTree.left)
    #     return left and right



        if not root:
            return True
        nodeList = [root.left,root.right]
        while nodeList:
            symmetricLeft = nodeList.pop(0)
            symmetricRight = nodeList.pop(0)
            if not symmetricLeft and not symmetricRight:
                continue
            if not symmetricLeft or not symmetricRight:
                return False
            if symmetricLeft.val != symmetricRight.val:
                return False
            nodeList.append(symmetricLeft.left)
            nodeList.append(symmetricRight.right)
            nodeList.append(symmetricLeft.right)
            nodeList.append(symmetricRight.left)
        return True
