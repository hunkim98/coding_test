from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # dfs with queue. If you want to
    queue = deque()

    queue.append(root)

    while len(queue) > 0:
        item = queue.pop()
        # we will dfs to the left
        left_node = item.left
        right_node = item.right

        item.right = left_node
        item.left = right_node

        if left_node is not None:
            queue.append(left_node)

        if right_node is not None:
            queue.append(right_node)

    return root


if __name__ == "__main__":
    child_1 = TreeNode(1)
    child_2 = TreeNode(3)
    root_1 = TreeNode(2, child_1, child_2)
    inverted_1 = invertTree(root_1)
    assert inverted_1.val == 2
    assert inverted_1.left.val == 3
    assert inverted_1.right.val == 1
