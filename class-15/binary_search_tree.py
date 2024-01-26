from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):

        # wrap value in Node
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        def walk(node_to_ask, node_to_add):
            """
            Look for the right spot to "sit" aka be added
            inspect each node and either
            a: "sit" next to it in correct spot
            b: move on in the correct direction
            """

            if node_to_add.value < node_to_ask.value:
                if node_to_ask.left is None:
                    node_to_ask.left = node_to_add
                else:
                    walk(node_to_ask.left, node_to_add)
            elif node_to_add.value >= node_to_ask.value: # >= value
                if node_to_ask.right is None:
                    node_to_ask.right = node_to_add
                else:
                    walk(node_to_ask.right, node_to_add)


        walk(self.root, new_node)
