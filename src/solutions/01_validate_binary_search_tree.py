from __future__ import annotations


class Node:
    def __init__(self, value: int, left: Node | None = None, right: Node | None = None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def validate_bst(self, root: Node | None) -> bool:
        return self._validate_bst(root, float("-inf"), float("inf"))

    def _validate_bst(
        self, root: Node | None, min_value: float, max_value: float
    ) -> bool:
        if root is None:
            return True

        if root.value < min_value or root.value > max_value:
            return False

        return self._validate_bst(
            root.left, min_value, root.value
        ) and self._validate_bst(root.right, root.value, max_value)


if __name__ == "__main__":
    #   5
    #  / \
    # 4   7
    node = Node(5)
    node.left = Node(4)
    node.right = Node(7)
    assert Solution().validate_bst(node)

    #   5
    #  / \
    # 4   7
    #    /
    #   2
    node = Node(5)
    node.left = Node(4)
    node.right = Node(7)
    node.right.left = Node(2)
    assert not Solution().validate_bst(node)
