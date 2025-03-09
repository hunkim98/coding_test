from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


sorting = []
isValidResult = True


def traverse(root):
    global sorting
    global isValidResult
    if isValidResult is False:
        return

    if root.left is not None:
        traverse(root.left)

    if len(sorting) >= 1 and root.val < sorting[len(sorting) - 1]:
        isValidResult = False

    sorting.append(root.val)

    if root.right is not None:
        traverse(root.right)


def isValidBST(root: Optional[TreeNode]) -> bool:
    global isValidResult
    traverse(root)
    return isValidResult


if __name__ == "__main__":
    level_2_left = TreeNode(3)
    level_2_right = TreeNode(6)
    level_1_right = TreeNode(4, level_2_left, level_2_right)
    level_1_left = TreeNode(1)
    root = TreeNode(5, level_1_left, level_1_right)
    result = isValidBST(root)
    assert result == False
