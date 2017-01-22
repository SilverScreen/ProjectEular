
class Tree(object):
    def __init__(self):
        self.node_1 = Node(left=None, right=None, data=8)
        self.node_2 = Node(left=None, right=None, data=5)
        self.node_3 = Node(left=None, right=None, data=9)
        self.node_4 = Node(left=None, right=None, data=3)

        self.node_5 = Node(left=self.node_1, right=self.node_2, data=2)
        self.node_6 = Node(left=self.node_2, right=self.node_3, data=4)
        self.node_7 = Node(left=self.node_3, right=self.node_4, data=6)

        self.node_8 = Node(left=self.node_5, right=self.node_6, data=7)
        self.node_9 = Node(left=self.node_6, right=self.node_7, data=4)

        self.root_node = Node(left=self.node_8, right=self.node_9, data=3)

        self.maximum_path = 0

    def find_maximum_path(self, current_node, counter):
        # print(current_node.data)
        counter += current_node.data
        left_node = current_node.left
        right_node = current_node.right

        if left_node:
            self.find_maximum_path(left_node, counter)
        else:
            return counter
        if right_node:
            self.find_maximum_path(right_node, counter)
        else:
            return counter


class Node(object):
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data


def main():
    number_tree = Tree()
    total = number_tree.find_maximum_path(current_node=number_tree.root_node, counter=0)
    print(total)


main()
