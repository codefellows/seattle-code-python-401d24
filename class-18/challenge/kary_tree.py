from data_structures.queue import Queue


class KaryTree:
    """
    Tree that handles nodes with "K" children
    Typically "K" means 3 or more
    Though you could refine this class to mean an exact number
    """
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection

    def clone(self):

        def walk(source_node):
            if source_node is None:
                return

            clone_node = Node(source_node.value)

            for source_child in source_node.children:
                cloned_child = walk(source_child)
                if cloned_child:
                    clone_node.children.append(cloned_child)

            return clone_node

        cloned_tree = KaryTree()
        cloned_tree.root = walk(self.root)

        return cloned_tree


class Node:
    """
    K-Ary Tree Node
    The number of children nodes is not restricted
    """

    def __init__(self, value):
        self.value = value
        self.children = []
