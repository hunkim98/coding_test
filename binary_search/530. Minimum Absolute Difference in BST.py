from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


sorted_node_vals = []


def traverse(root: TreeNode):
    global sorted_node_vals
    if root.left:
        traverse(root.left)
    sorted_node_vals.append(root.val)
    if root.right:
        traverse(root.right)


def getMinimumDifference(root: TreeNode):
    global sorted_node_vals
    # we should first sort
    traverse(root)
    min_diff = float("inf")

    for i in range(1, len(sorted_node_vals)):
        diff = abs(sorted_node_vals[i] - sorted_node_vals[i - 1])
        if diff < min_diff:
            min_diff = diff

    return min_diff


if __name__ == "__main__":
    level3_left = TreeNode(1)
    level3_right = TreeNode(3)
    level2_left = TreeNode(2, level3_left, level3_right)
    level2_right = TreeNode(6)
    root = TreeNode(4, level2_left, level2_right)
    assert getMinimumDifference(root) == 1
