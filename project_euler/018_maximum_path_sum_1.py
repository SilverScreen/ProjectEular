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

        # Row 13
        self.node_13_1 = Node(left=self.node_14_1, right=self.node_14_2, data=91)
        self.node_13_2 = Node(left=self.node_14_2, right=self.node_14_3, data=71)
        self.node_13_3 = Node(left=self.node_14_3, right=self.node_14_4, data=52)
        self.node_13_4 = Node(left=self.node_14_4, right=self.node_14_5, data=38)
        self.node_13_5 = Node(left=self.node_14_5, right=self.node_14_6, data=17)
        self.node_13_6 = Node(left=self.node_14_6, right=self.node_14_7, data=14)
        self.node_13_7 = Node(left=self.node_14_7, right=self.node_14_8, data=91)
        self.node_13_8 = Node(left=self.node_14_8, right=self.node_14_9, data=43)
        self.node_13_9 = Node(left=self.node_14_9, right=self.node_14_10, data=58)
        self.node_13_10 = Node(left=self.node_14_10, right=self.node_14_11, data=50)
        self.node_13_11 = Node(left=self.node_14_11, right=self.node_14_12, data=27)
        self.node_13_12 = Node(left=self.node_14_12, right=self.node_14_13, data=29)
        self.node_13_13 = Node(left=self.node_14_13, right=self.node_14_14, data=48)

        # Row 12
        self.node_12_1 = Node(left=self.node_13_1, right=self.node_13_2, data=70)
        self.node_12_2 = Node(left=self.node_13_2, right=self.node_13_3, data=11)
        self.node_12_3 = Node(left=self.node_13_3, right=self.node_13_4, data=33)
        self.node_12_4 = Node(left=self.node_13_4, right=self.node_13_5, data=28)
        self.node_12_5 = Node(left=self.node_13_5, right=self.node_13_6, data=77)
        self.node_12_6 = Node(left=self.node_13_6, right=self.node_13_7, data=73)
        self.node_12_7 = Node(left=self.node_13_7, right=self.node_13_8, data=17)
        self.node_12_8 = Node(left=self.node_13_8, right=self.node_13_9, data=78)
        self.node_12_9 = Node(left=self.node_13_9, right=self.node_13_10, data=39)
        self.node_12_10 = Node(left=self.node_13_10, right=self.node_13_11, data=68)
        self.node_12_11 = Node(left=self.node_13_11, right=self.node_13_12, data=17)
        self.node_12_12 = Node(left=self.node_13_12, right=self.node_13_13, data=57)

        # Row 11
        self.node_11_1 = Node(left=self.node_12_1, right=self.node_12_2, data=53)
        self.node_11_2 = Node(left=self.node_12_2, right=self.node_12_3, data=71)
        self.node_11_3 = Node(left=self.node_12_3, right=self.node_12_4, data=44)
        self.node_11_4 = Node(left=self.node_12_4, right=self.node_12_5, data=65)
        self.node_11_5 = Node(left=self.node_12_5, right=self.node_12_6, data=25)
        self.node_11_6 = Node(left=self.node_12_6, right=self.node_12_7, data=43)
        self.node_11_7 = Node(left=self.node_12_7, right=self.node_12_8, data=91)
        self.node_11_8 = Node(left=self.node_12_8, right=self.node_12_9, data=52)
        self.node_11_9 = Node(left=self.node_12_9, right=self.node_12_10, data=97)
        self.node_11_10 = Node(left=self.node_12_10, right=self.node_12_11, data=51)
        self.node_11_11 = Node(left=self.node_12_11, right=self.node_12_12, data=14)

        # Row 10
        self.node_10_1 = Node(left=self.node_11_1, right=self.node_11_2, data=41)
        self.node_10_2 = Node(left=self.node_11_2, right=self.node_11_3, data=48)
        self.node_10_3 = Node(left=self.node_11_3, right=self.node_11_4, data=72)
        self.node_10_4 = Node(left=self.node_11_4, right=self.node_11_5, data=33)
        self.node_10_5 = Node(left=self.node_11_5, right=self.node_11_6, data=47)
        self.node_10_6 = Node(left=self.node_11_6, right=self.node_11_7, data=32)
        self.node_10_7 = Node(left=self.node_11_7, right=self.node_11_8, data=37)
        self.node_10_8 = Node(left=self.node_11_8, right=self.node_11_9, data=16)
        self.node_10_9 = Node(left=self.node_11_9, right=self.node_11_10, data=94)
        self.node_10_10 = Node(left=self.node_11_10, right=self.node_11_11, data=29)

        # Row 9
        self.node_9_1 = Node(left=self.node_10_1, right=self.node_10_2, data=41)
        self.node_9_2 = Node(left=self.node_10_2, right=self.node_10_3, data=41)
        self.node_9_3 = Node(left=self.node_10_3, right=self.node_10_4, data=26)
        self.node_9_4 = Node(left=self.node_10_4, right=self.node_10_5, data=56)
        self.node_9_5 = Node(left=self.node_10_5, right=self.node_10_6, data=83)
        self.node_9_6 = Node(left=self.node_10_6, right=self.node_10_7, data=40)
        self.node_9_7 = Node(left=self.node_10_7, right=self.node_10_8, data=80)
        self.node_9_8 = Node(left=self.node_10_8, right=self.node_10_9, data=70)
        self.node_9_9 = Node(left=self.node_10_9, right=self.node_10_10, data=33)

        # Row 8
        self.node_8_1 = Node(left=self.node_9_1, right=self.node_9_2, data=99)
        self.node_8_2 = Node(left=self.node_9_2, right=self.node_9_3, data=65)
        self.node_8_3 = Node(left=self.node_9_3, right=self.node_9_4, data=4)
        self.node_8_4 = Node(left=self.node_9_4, right=self.node_9_5, data=28)
        self.node_8_5 = Node(left=self.node_9_5, right=self.node_9_6, data=6)
        self.node_8_6 = Node(left=self.node_9_6, right=self.node_9_7, data=16)
        self.node_8_7 = Node(left=self.node_9_7, right=self.node_9_8, data=70)
        self.node_8_8 = Node(left=self.node_9_8, right=self.node_9_9, data=92)

        # Row 7
        self.node_7_1 = Node(left=self.node_8_1, right=self.node_8_2, data=88)
        self.node_7_2 = Node(left=self.node_8_2, right=self.node_8_3, data=2)
        self.node_7_3 = Node(left=self.node_8_3, right=self.node_8_4, data=77)
        self.node_7_4 = Node(left=self.node_8_4, right=self.node_8_5, data=73)
        self.node_7_5 = Node(left=self.node_8_5, right=self.node_8_6, data=7)
        self.node_7_6 = Node(left=self.node_8_6, right=self.node_8_7, data=63)
        self.node_7_7 = Node(left=self.node_8_7, right=self.node_8_8, data=67)

        # Row 7
        self.node_6_1 = Node(left=self.node_7_1, right=self.node_7_2, data=19)
        self.node_6_2 = Node(left=self.node_7_2, right=self.node_7_3, data=1)
        self.node_6_3 = Node(left=self.node_7_3, right=self.node_7_4, data=23)
        self.node_6_4 = Node(left=self.node_7_4, right=self.node_7_5, data=75)
        self.node_6_5 = Node(left=self.node_7_5, right=self.node_7_6, data=3)
        self.node_6_6 = Node(left=self.node_7_6, right=self.node_7_7, data=34)

        # Row 7
        self.node_5_1 = Node(left=self.node_6_1, right=self.node_6_2, data=20)
        self.node_5_2 = Node(left=self.node_6_2, right=self.node_6_3, data=4)
        self.node_5_3 = Node(left=self.node_6_3, right=self.node_6_4, data=82)
        self.node_5_4 = Node(left=self.node_6_4, right=self.node_6_5, data=47)
        self.node_5_5 = Node(left=self.node_6_5, right=self.node_6_6, data=65)

        # Row 7
        self.node_4_1 = Node(left=self.node_5_1, right=self.node_5_2, data=18)
        self.node_4_2 = Node(left=self.node_5_2, right=self.node_5_3, data=35)
        self.node_4_3 = Node(left=self.node_5_3, right=self.node_5_4, data=87)
        self.node_4_4 = Node(left=self.node_5_4, right=self.node_5_5, data=10)

        # Row 7
        self.node_3_1 = Node(left=self.node_4_1, right=self.node_4_2, data=17)
        self.node_3_2 = Node(left=self.node_4_2, right=self.node_4_3, data=47)
        self.node_3_3 = Node(left=self.node_4_3, right=self.node_4_4, data=82)

        # Row 7
        self.node_2_1 = Node(left=self.node_3_1, right=self.node_3_2, data=95)
        self.node_2_2 = Node(left=self.node_3_2, right=self.node_3_3, data=64)

        self.root_node = Node(left=self.node_2_1, right=self.node_2_2, data=75)

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
