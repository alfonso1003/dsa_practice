from __future__ import annotations


class Node:
    def __init__(self, val: int, next_node: Node | None = None):
        self.value = val
        self.next = next_node

    def __eq__(self, other: Node) -> bool:
        if not isinstance(other, Node):
            return False
        return self.value == other.value and self.next == other.next


class Solution:
    def __init__(self, method: str = "iterative"):
        if method not in {"iterative", "recursive"}:
            raise ValueError("Invalid method. Choose 'iterative' or 'recursive'.")
        self.method = method

    def add_two_nodes(self, n1: Node | None, n2: Node | None) -> Node | None:
        if self.method == "recursive":
            return self._add_two_nodes_recursive(n1, n2, 0)
        return self._add_two_nodes_iterative(n1, n2)

    def _add_two_nodes_recursive(
        self, n1: Node | None, n2: Node | None, carry: int
    ) -> Node | None:
        if not n1 and not n2 and carry == 0:
            return None

        val1 = n1.value if n1 else 0
        val2 = n2.value if n2 else 0
        carry, value = divmod(val1 + val2 + carry, 10)

        result = Node(value)

        next1 = n1.next if n1 else None
        next2 = n2.next if n2 else None
        result.next = self._add_two_nodes_recursive(next1, next2, carry)

        return result

    def _add_two_nodes_iterative(self, n1: Node | None, n2: Node | None) -> Node | None:
        carry = 0
        head: Node | None = None
        tail: Node | None = None

        while n1 or n2 or carry:
            val1 = n1.value if n1 else 0
            val2 = n2.value if n2 else 0

            carry, value = divmod(val1 + val2 + carry, 10)
            new_node = Node(value)

            if not head:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = tail.next

            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None

        return head


if __name__ == "__main__":
    # Example usage:
    # 546 + 837 = 1383 (reversed: 6->4->5 + 7->3->8 = 3->8->3->1)
    l1 = Node(6)
    l1.next = Node(4)
    l1.next.next = Node(5)

    l2 = Node(7)
    l2.next = Node(3)
    l2.next.next = Node(8)

    # Create the expected linked list: 3 -> 8 -> 3 -> 1
    expected = Node(3)
    expected.next = Node(8)
    expected.next.next = Node(3)
    expected.next.next.next = Node(1)

    iterative_solution = Solution("iterative")
    iterative_answer = iterative_solution.add_two_nodes(l1, l2)

    recursive_solution = Solution("recursive")
    recursive_answer = recursive_solution.add_two_nodes(l1, l2)

    assert iterative_answer == expected
    assert recursive_answer == expected
    assert iterative_answer == recursive_answer
