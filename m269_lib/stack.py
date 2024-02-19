"""This module provides implementations of the Stack ADT."""


class PythonListStack:
    """A last-in, first-out sequence of objects, implemented with a Python list.

    This class can also be imported as `Stack`. Usage example:
    >>> from m269_lib import Stack
    >>> stack = Stack()
    >>> for n in range(3):
    ...     stack.push(n)
    ...     print("Pushed", stack.top())
    Pushed 0
    Pushed 1
    Pushed 2
    >>> while stack.size() > 0:
    ...     print("Popped", stack.pop())
    Popped 2
    Popped 1
    Popped 0
    """

    def __init__(self) -> None:
        """Initialise the stack to be empty."""
        self._members = []

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._members)

    def top(self) -> object:
        """Return the top item in the stack.

        Preconditions: `self.size() > 0`
        Complexity: O(1)
        """
        return self._members[-1]

    def pop(self) -> object:
        """Remove and return the top item from the stack.

        Preconditions: `self.size() > 0`
        Complexity: O(1)
        """
        return self._members.pop(-1)

    def push(self, item: object) -> None:
        """Put the given item on top of the stack.

        Postconditions: `self.top() == item`
        Complexity: O(1)
        """
        self._members.append(item)


class LinkedListStack:
    """A last-in, first-out sequence of objects, implemented with a linked list.

    Usage example:
    >>> from m269_lib import LinkedListStack
    >>> stack = LinkedListStack()
    >>> for n in range(3):
    ...     stack.push(n)
    ...     print("Pushed", stack.top())
    Pushed 0
    Pushed 1
    Pushed 2
    >>> while stack.size() > 0:
    ...     print("Popped", stack.pop())
    Popped 2
    Popped 1
    Popped 0
    """

    class _Node:
        """A node in a linked list."""

        def __init__(self, item: object) -> None:
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self) -> None:
        """Initialise the stack to be empty."""
        self._head = None
        self._length = 0

    def size(self) -> int:
        """Return the number of items in the stack.

        Complexity: O(1)
        """
        return self._length

    def top(self) -> object:
        """Return the top item in the stack.

        Preconditions: `self.size() > 0`
        Complexity: O(1)
        """
        return self._head.item

    def pop(self) -> object:
        """Remove and return the top item from the stack.

        Preconditions: `self.size() > 0`
        Complexity: O(1)
        """
        item = self._head.item
        self._head = self._head.next
        self._length = self._length - 1
        return item

    def push(self, item: object) -> None:
        """Put the given item on top of the stack.

        Postconditions: `self.top() == item`
        Complexity: O(1)
        """
        node = LinkedListStack._Node(item)
        node.next = self._head
        self._head = node
        self._length = self._length + 1
