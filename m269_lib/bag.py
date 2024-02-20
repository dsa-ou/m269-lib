"""This module implements the Bag (Multiset) ADT."""

from typing import Hashable, Iterable  # noqa: UP035 # allowed


class PythonDictBag:
    """An unordered collection of items, implemented with a Python dictionary.

    The bag may have multiple copies of each item.

    This class can also be imported as `Bag`. Usage example:

    >>> from m269_lib import Bag
    >>> text = Bag("to be or not to be")
    >>> text.size()                                 # number of characters
    18
    >>> text.copies(" ") + 1                        # number of words
    6
    >>> text.remove("o")                            # remove 1 copy of "o"
    >>> text.remove("n")                            # remove the only "n"
    >>> text.add("?")                               # add 1 copy of "?"
    >>> text.as_dict()                              # inspect for debugging
    {'t': 3, 'o': 3, ' ': 5, 'b': 2, 'e': 2, 'r': 1, '?': 1}

    Further examples are given in the method descriptions below.
    """

    def __init__(self, items: Iterable[Hashable]) -> None:
        """Initialize the bag with the given items.

        Use an empty collection to create an empty bag, e.g. `Bag([])`.

        Complexity: O(`len(items)`).
        """
        self._copies = dict()
        for item in items:
            self.add(item)

    def copies(self, item: Hashable) -> int:
        """Return how many times `item` occurs in the bag.

        Complexity: O(1).
        """
        if item in self._copies:
            return self._copies[item]
        else:
            return 0

    def size(self) -> int:
        """Return how many items (total copies) the bag has.

        Complexity: O(*n*), with *n* the number of unique items in the bag.
        """
        total = 0
        for item in self._copies:
            total = total + self._copies[item]
        return total

    def as_dict(self) -> dict:
        """Return the underlying dictionary.

        The dictionary can be used to inspect the bag,
        for debugging or other purposes, like:

        >>> from m269_lib import Bag
        >>> pepper = Bag("pepper")
        >>> for item in pepper.as_dict():           # iterate over the unique items
        ...     print(item, "occurs", pepper.copies(item), "times")
        p occurs 3 times
        e occurs 2 times
        r occurs 1 times
        >>> proper = Bag("proper")
        >>> pepper.as_dict() == proper.as_dict()    # check bag equality
        False

        Complexity: O(*n*), with *n* the number of unique items in the bag.
        """
        # Return a copy of the dictionary to avoid modifying the bag.
        return dict(self._copies)

    def add(self, item: Hashable) -> None:
        """Add one more copy (or the first copy) of `item` to the bag.

        Complexity: O(1).
        """
        if item in self._copies:
            self._copies[item] = self._copies[item] + 1
        else:
            self._copies[item] = 1

    def remove(self, item: Hashable) -> None:
        """Remove one copy of `item` from the bag.

        Preconditions: `self.copies(item) > 0`.
        Complexity: O(1).
        """
        if self._copies[item] == 1:
            self._copies.pop(item)
        else:
            self._copies[item] = self._copies[item] - 1

    def union(self, other: "PythonDictBag") -> "PythonDictBag":
        """Return a new bag with the items that occur in either bag.

        If an item occurs *m* times in one bag and *n* times in the other,
        then it occurs max(*m*, *n*) times in the union.

        >>> from m269_lib import Bag
        >>> bag1 = Bag("abcc")
        >>> bag2 = Bag("bbcd")
        >>> (bag1.union(bag2)).as_dict()
        {'a': 1, 'c': 2, 'b': 2, 'd': 1}

        Complexity: O(*s* + *o*),
        with *s* and *o* the number of unique items in the bags.
        """
        new_bag = PythonDictBag([])
        # Add the maximum of each item's occurrences in the two bags.
        for member in self._copies:
            if self.copies(member) >= other.copies(member):
                new_bag._copies[member] = self.copies(member)
        for member in other._copies:
            if other.copies(member) > self.copies(member):
                new_bag._copies[member] = other.copies(member)
        return new_bag

    def intersection(self, other: "PythonDictBag") -> "PythonDictBag":
        """Return a new bag with the common items of both bags.

        If an item occurs *m* times in one bag and *n* times in the other,
        then it occurs min(*m*, *n*) times in the intersection.

        >>> from m269_lib import Bag
        >>> bag1 = Bag("abcc")
        >>> bag2 = Bag("bbcd")
        >>> (bag1.intersection(bag2)).as_dict()     # only 1 b and 1 c are common
        {'b': 1, 'c': 1}
        >>> (Bag([]).intersection(bag2)).size()     # no common items with an empty bag
        0

        Complexity: O(min(*s*, *o*)),
        with *s* and *o* the number of unique items in the bags.
        """
        new_bag = PythonDictBag([])
        if len(self._copies) >= len(other._copies):
            larger = self
            smaller = other
        else:
            larger = other
            smaller = self
        for item in smaller._copies:
            common = min(smaller.copies(item), larger.copies(item))
            if common > 0:
                new_bag._copies[item] = common
        return new_bag

    def difference(self, other: "PythonDictBag") -> "PythonDictBag":
        """Return a new bag with the items that are in `self` but not in `other`.

        If an item occurs *m* times in `self` and *n* times in `other`,
        then it occurs max(0, *m* - *n*) times in the difference.

        >>> from m269_lib import Bag
        >>> bag1 = Bag("abcc")
        >>> bag2 = Bag("bbcd")
        >>> (bag1.difference(bag2)).as_dict()
        {'a': 1, 'c': 1}

        Complexity: O(*s*), with *s* the number of unique items in `self`.
        """
        new_bag = PythonDictBag([])
        for item in self._copies:
            extra = self.copies(item) - other.copies(item)
            if extra > 0:
                new_bag._copies[item] = extra
        return new_bag

    def included_in(self, other: "PythonDictBag") -> bool:
        """Check if each item of `self` occurs the same or more times in `other`.

        >>> from m269_lib import Bag
        >>> vowels = Bag("aeiou")
        >>> vowels.included_in(Bag("are you in?"))
        True
        >>> vowels.included_in(Bag("are you away?"))
        False

        Complexity: O(*s*), with *s* the number of unique items in `self`.
        """
        for item in self._copies:
            if self.copies(item) > other.copies(item):
                return False
        return True
