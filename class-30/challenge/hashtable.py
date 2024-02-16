from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size

    def set(self, key, value):
        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self._buckets[index] = bucket

        current = bucket.head

        while current:
            candidate_drop = current.value
            if candidate_drop[0] == key:
                # found preexisting drop
                candidate_drop[1] = value  # update the value
                return

        drop = [key, value]  # no prexisting drop, add the drop aka key-value pair
        bucket.insert(drop)

    def get(self, key):
        index = self._hash(key)

        bucket = self._buckets[index]

        if bucket is None:
            return None

        current = bucket.head

        while current:
            drop = current.value  # key value pair
            if drop[0] == key:
                return drop[1]

            current = current.next

        return None

    def keys(self):
        """
        return list of keys
        """
        key_list = []  # list of strings

        for bucket in self._buckets:  # list of LinkedLists (or None)
            if bucket:  # LinkedList
                current = bucket.head  # Node
                while current:
                    drop = current.value  # List of 2 items [key, value]
                    key_list.append(drop[0])
                    current = current.next

        return key_list

    def has(self, key):
        for bucket in self._buckets:  # list of LinkedLists (or None)
            if bucket:  # LinkedList
                current = bucket.head  # Node
                while current:
                    drop = current.value  # List of 2 items [key, value]
                    if drop[0] == key:
                        return True

                    current = current.next

        return False

    def _hash(self, key):
        """
        Add all the ASCII values together.
        Multiply it by a prime number such as 599.
        Use modulo to get the remainder of the result, when divided by the total size of the array.
        """
        index = 0
        for char in key:
            index += ord(char)
        index *= 599
        index = index % self._size

        return index
