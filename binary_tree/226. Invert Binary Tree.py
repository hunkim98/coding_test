from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    new_left = invertTree(root.right)
    new_right = invertTree(root.left)
    root.left = new_left
    root.right = new_right
    return root


if __name__ == "__main__":
    child_1 = TreeNode(1)
    child_2 = TreeNode(3)
    root_1 = TreeNode(2, child_1, child_2)
    inverted_1 = invertTree(root_1)
    assert inverted_1.val == 2
    assert inverted_1.left.val == 3
    assert inverted_1.right.val == 1
