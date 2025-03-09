from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


up_cnt = 0
kth = 0
final_val = None


def traverse(root):
    global up_cnt
    global kth
    global final_val

    if final_val is not None:
        return

    if root.left is not None:
        traverse(root.left)
    up_cnt += 1
    if kth == up_cnt:
        final_val = root.val
    if root.right is not None:
        traverse(root.right)


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    global up_cnt
    global kth
    global final_val
    kth = k
    traverse(root)
    return final_val


if __name__ == "__main__":
    level2_right = TreeNode(2)
    level1_left = TreeNode(1)
    level1_right = TreeNode(4)
    root = TreeNode(3, level1_left, level2_right)
    assert kthSmallest(root, 1) == 1
