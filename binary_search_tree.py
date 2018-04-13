from collections import defaultdict

class Node:
    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.left = None
        self.right = None


class BinarySearchTree:
    levels_list = []
    dict_values = defaultdict(list)

    def __init__(self):
        self.root = None;

    def push(self, value):
        if self.root is None:
            self.root = Node(value, 0)
        else:
            self.push_helper(value, self.root, 1)

    def push_helper(self, value, node, level):
        if value < node.value:
            level += 1
            if node.left is None:
                node.left = Node(value,level)
            else:
                self.push_helper(value, node.left, level)
        elif value > node.value:
            level += 1
            if node.right is None:
                node.right = Node(value, level)
            else:
                self.push_helper(value, node.right, level)
        else:
            print("Error: value is already in the tree")

    def get_levels(self):
        self.levels_list = []
        if self.root is None:
            self.levels_list.append(0)
        else:
            if self.root.left is not None:
                self.get_levels_helper(self.root.left, 1)
            if self.root.right is not None:
                self.get_levels_helper(self.root.right, 1)
        return max(self.levels_list)

    def get_levels_helper(self, node, level):
        if node.left is None:
            self.levels_list.append(level)
        else:
            level += 1
            self.get_levels_helper(node.left, level)
        if node.right is None:
            self.levels_list.append(level)
        else:
            level += 1
            self.get_levels_helper(node.right, level)

    def get_values(self):
        self.dict_values = defaultdict(list)
        if self.root is not None:
            self.dict_values["Level_1"].append(self.root.value)
            if self.root.left is not None:
                self.get_values_helper(self.root.left)
            if self.root.right is not None:
                self.get_values_helper(self.root.right)
        return dict(self.dict_values)

    def get_values_helper(self, node):
        self.dict_values["Level_{}".format(node.level)].append(node.value)
        if node.left is not None:
            self.get_values_helper(node.left)
        if node.right is not None:
            self.get_values_helper(node.right)

    def is_complete(self):
        tmp_dict = self.get_values()
        final_boolean = True
        for x in range(2, len(tmp_dict) + 1):
            if 2 * x == len(tmp_dict["Level_{}".format(x)]) or x == len(tmp_dict) and (len(tmp_dict["Level_{}".format(x)]) % 2 == 0) and (len(tmp_dict["Level_{}".format(x)]) != 1):
                final_boolean = True
            else:
                final_boolean = False
        return final_boolean


testTree = BinarySearchTree()
testTree.push(7)
testTree.push(3)
testTree.push(8)
testTree.push(1)
testTree.push(4)
testTree.get_levels()
print(testTree.get_values())
print(testTree.is_complete())
#       7
#   3       8
#1      4