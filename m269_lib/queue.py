"""This module provides implementations of the Queue ADT."""


class PythonListQueue:
    """A first-in, first-out sequence of objects, implemented with a Python list.

    Usage example:
    >>> from m269_lib import PythonListQueue
    >>> queue = PythonListQueue()
    >>> for n in range(3):
    ...     queue.enqueue(n)
    ...     print("Front:", queue.front())
    Front: 0
    Front: 0
    Front: 0
    >>> while queue.size() > 0:
    ...     print("Dequeuing", queue.dequeue())
    Dequeuing 0
    Dequeuing 1
    Dequeuing 2
    """

    def __init__(self) -> None:
        """Initialise the queue to be empty."""
        self._members = []

    def size(self) -> int:
        """Return the number of items in the queue.

        Complexity: O(1).
        """
        return len(self._members)

    def front(self) -> object:
        """Return the item at the front of the queue.

        Preconditions: `self.size() > 0`.
        Complexity: O(1).
        """
        return self._members[0]

    def enqueue(self, item: object) -> None:
        """Add `item` to the back of the queue.

        Complexity: O(1).
        """
        self._members.append(item)

    def dequeue(self) -> object:
        """Remove and return the item at the front of the queue.

        Preconditions: `self.size() > 0`.
        Complexity: O(`self.size()`).
        """
        return self._members.pop(0)


class LinkedListQueue:
    """A last-in, first-out sequence of objects, implemented with a linked list.

    This class can also be imported as `Queue`. Usage example:
    >>> from m269_lib import Queue
    >>> queue = Queue()
    >>> for n in range(3):
    ...     queue.enqueue(n)
    ...     print("Front:", queue.front())
    Front: 0
    Front: 0
    Front: 0
    >>> while queue.size() > 0:
    ...     print("Dequeuing", queue.dequeue())
    Dequeuing 0
    Dequeuing 1
    Dequeuing 2
    """

    class _Node:
        """A node in a linked list."""

        def __init__(self, item: object) -> None:
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self) -> None:
        """Initialise the queue to be empty."""
        self._head = None
        self._last = None
        self._length = 0

    def size(self) -> int:
        """Return the number of items in the queue.

        Complexity: O(1).
        """
        return self._length

    def front(self) -> object:
        """Return the item at the front of the queue.

        Preconditions: `self.size() > 0`.
        Complexity: O(1).
        """
        return self._head.item

    def enqueue(self, item: object) -> None:
        """Add `item` to the back of the queue.

        Complexity: O(1).
        """
        node = LinkedListQueue._Node(item)
        if self._length == 0:
            self._head = node
        else:
            self._last.next = node
        self._last = node
        self._length = self._length + 1

    def dequeue(self) -> object:
        """Remove and return the item at the front of the queue.

        Preconditions: `self.size() > 0`.
        Complexity: O(1).
        """
        item = self._head.item
        self._head = self._head.next
        if self._head == None:
            self._last = None
        self._length = self._length - 1
        return item
