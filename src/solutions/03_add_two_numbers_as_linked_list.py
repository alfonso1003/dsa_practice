class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.value == other.value and self.next == other.next


class Solution:
    def add_two_nodes(self, n1, n2):
        return self._add_two_nodes_recursive(n1, n2, 0)

    def _add_two_nodes_recursive(self, n1, n2, carry):
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


# Example usage:
# 546 + 837 = 1383 (reversed: 6->4->5 + 7->3->8 = 3->8->3->1)
l1 = Node(6)
l1.next = Node(4)
l1.next.next = Node(5)

l2 = Node(7)
l2.next = Node(3)
l2.next.next = Node(8)

solution = Solution()
answer = solution.add_two_nodes(l1, l2)

# Create the expected linked list: 3 -> 8 -> 3 -> 1
expected = Node(3)
expected.next = Node(8)
expected.next.next = Node(3)
expected.next.next.next = Node(1)

assert answer == expected, "Test failed: Result does not match expected output."
