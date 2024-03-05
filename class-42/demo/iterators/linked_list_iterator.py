class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):  # [a,b,c] => [a] -> [b] -> [c] -> None
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)


    def __iter__(self):

        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()


    def __str__(self):
        out = ""
        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"



    def __len__(self):
        # DANGER: not O(1) - better IRL to track a self.length

        length = 0
        for _ in self:
            length += 1

        return length

        # or weird one liner
        # return len(list(iter(self)))

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):

        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError





class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
