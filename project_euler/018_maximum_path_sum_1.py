
class Tree(object):
    def __init__(self):
        # self.node_1 = Node(left=None, right=None, data=8)
        # self.node_2 = Node(left=None, right=None, data=5)
        # self.node_3 = Node(left=None, right=None, data=9)
        # self.node_4 = Node(left=None, right=None, data=3)
        #
        # self.node_5 = Node(left=self.node_1, right=self.node_2, data=2)
        # self.node_6 = Node(left=self.node_2, right=self.node_3, data=4)
        # self.node_7 = Node(left=self.node_3, right=self.node_4, data=6)
        #
        # self.node_8 = Node(left=self.node_5, right=self.node_6, data=7)
        # self.node_9 = Node(left=self.node_6, right=self.node_7, data=4)
        #
        # self.root_node = Node(left=self.node_8, right=self.node_9, data=3)

        # Row 15
        self.node_15_1 = Node(left=None, right=None, data=4)
        self.node_15_2 = Node(left=None, right=None, data=62)
        self.node_15_3 = Node(left=None, right=None, data=98)
        self.node_15_4 = Node(left=None, right=None, data=27)
        self.node_15_5 = Node(left=None, right=None, data=23)
        self.node_15_6 = Node(left=None, right=None, data=9)
        self.node_15_7 = Node(left=None, right=None, data=70)
        self.node_15_8 = Node(left=None, right=None, data=98)
        self.node_15_9 = Node(left=None, right=None, data=73)
        self.node_15_10 = Node(left=None, right=None, data=93)
        self.node_15_11 = Node(left=None, right=None, data=38)
        self.node_15_12 = Node(left=None, right=None, data=53)
        self.node_15_13 = Node(left=None, right=None, data=60)
        self.node_15_14 = Node(left=None, right=None, data=4)
        self.node_15_15 = Node(left=None, right=None, data=23)

        # Row 14
        self.node_14_1 = Node(left=self.node_15_1, right=self.node_15_2, data=63)
        self.node_14_2 = Node(left=self.node_15_2, right=self.node_15_3, data=66)
        self.node_14_3 = Node(left=self.node_15_3, right=self.node_15_4, data=4)
        self.node_14_4 = Node(left=self.node_15_4, right=self.node_15_5, data=68)
        self.node_14_5 = Node(left=self.node_15_5, right=self.node_15_6, data=89)
        self.node_14_6 = Node(left=self.node_15_6, right=self.node_15_7, data=53)
        self.node_14_7 = Node(left=self.node_15_7, right=self.node_15_8, data=67)
        self.node_14_8 = Node(left=self.node_15_8, right=self.node_15_9, data=30)
        self.node_14_9 = Node(left=self.node_15_9, right=self.node_15_10, data=73)
        self.node_14_10 = Node(left=self.node_15_10, right=self.node_15_11, data=16)
        self.node_14_11 = Node(left=self.node_15_11, right=self.node_15_12, data=69)
        self.node_14_12 = Node(left=self.node_15_12, right=self.node_15_13, data=87)
        self.node_14_13 = Node(left=self.node_15_13, right=self.node_15_14, data=40)
        self.node_14_14 = Node(left=self.node_15_14, right=self.node_15_15, data=31)


        self.maximum_path = 0

    def calculate_maximum_path(self, current_node, counter):
        counter += current_node.data
        left_node = current_node.left
        right_node = current_node.right

        if left_node:
            self.calculate_maximum_path(left_node, counter)
        else:
            if counter > self.maximum_path:
                self.maximum_path = counter

        if right_node:
            self.calculate_maximum_path(right_node, counter)
        else:
            if counter > self.maximum_path:
                self.maximum_path = counter


class Node(object):
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data


def main():
    number_tree = Tree()
    number_tree.calculate_maximum_path(current_node=number_tree.root_node, counter=0)
    print(number_tree.maximum_path)


main()
