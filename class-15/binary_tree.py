class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.root = None

    def pre_order(self):
        """
              a
          b      c
        d  e    f  g

        ["a",       "b", "d", "e",      "c", "f", "g"]

        root -> left -> right
        BUT "root" depends on context
        It's not necessarily same as root of overall tree

        """

        def walk(node):
            """
            task is

            return my result + left node's result + right node's result

            ["a"] + ["b","d","e"] + ["c","f","g"]

            return List

            """

            if node is None:
                return []

            my_result = [node.value]   # ["a"]
            left_result = walk(node.left) # [... whatever is collected to left ...] ["b","d","e"]
            right_result = walk(node.right)# [... whatever is collected to right ...] ["c","f","g"]

            # ["a"] + ["b","d","e"] + ["c","f","g"]
            return my_result + left_result + right_result


        return walk(self.root)

    def in_order(self):
        """
        left -> root -> right
        BUT "root" depends on context
        It's not necessarily same as root of overall tree
        """

        def walk(node):
            """
            task is

            return my result + left node's result + right node's result

            ["a"] + ["b","d","e"] + ["c","f","g"]

            return List

            """

            if node is None:
                return []

            left_result = walk(node.left) # [... whatever is collected to left ...] ["b","d","e"]
            my_result = [node.value]   # ["a"]
            right_result = walk(node.right)# [... whatever is collected to right ...] ["c","f","g"]

            # ["b","d","e"] + ["a"] + ["c","f","g"]
            return left_result + my_result + right_result


        return walk(self.root)

    def post_order(self):
        """
        left -> right -> root
        BUT "root" depends on context
        It's not necessarily same as root of overall tree
        """


        def walk(node):
            if node is None:
                return []

            left_result = walk(node.left) # [... whatever is collected to left ...] ["b","d","e"]
            right_result = walk(node.right)# [... whatever is collected to right ...] ["c","f","g"]
            my_result = [node.value]   # ["a"]


            return left_result + right_result + my_result


        return walk(self.root)



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

