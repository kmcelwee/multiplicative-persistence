"""
TODO
- collect helpful functions from variant and here into a utils file
- change tree -> trees


    methods
        build_tree
        max_height
        generate_histogram
        write_json(json_path) # nested form

"""

from anytree import Node, RenderTree
from functools import reduce

from MultiplicativePersistence import MpNumberVariant


class Tree:
    def __init__(self, collection):
        self.collection = collection
        self.node_dict = {x: Node(x) for x in range(0, 10)}

    def get_node(self, num):
        if num not in self.node_dict:
            raise Exception(f"The number {num} does not appear in this tree")
        return self.node_dict[num]

    def add_child(self, child_num):
        mp_list = self.get_mp_list(child_num)
        parent_node = self.get_node(mp_list[0])
        for num in mp_list[1:]:
            if num in self.node_dict:
                parent_node = self.get_node(num)
                continue

            new_node = Node(num, parent=parent_node)
            self.node_dict[num] = new_node

            parent_node = new_node

    def build_node_dict(self):
        node_dict = {}
        variants = self.collection.all_variants()

        for variant in variants:
            self.add_node_and_children(variant.base_10)

        return node_dict

    @classmethod
    def get_number_child(self, n):
        int_list = [int(x) for x in str(n)]
        return reduce((lambda x, y: x * y), int_list)

    @classmethod
    def get_mp_list(self, num):
        return_list = [num]
        this_num = num
        while len(str(this_num)) != 1:
            this_num = self.get_number_child(this_num)
            return_list.append(this_num)
        return list(reversed(return_list))
