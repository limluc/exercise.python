""" Node is defined as
"""
import sys


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_binary_search_tree_(root):
    # Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.
    return check_for_binary_tree(root, 0, -sys.maxint)


def check_for_binary_tree(root, min, max):
    if root is None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return check_for_binary_tree(root.left, min, root.data) and check_for_binary_tree(root.right, root.data, max)
