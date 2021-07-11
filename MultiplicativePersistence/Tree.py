"""
TODO
Refactor
- collect helpful functions from variant and here into a utils file
- change tree -> trees
- remove mp prefixes

methods
    write_json(json_path) # nested form
    read_json(json_path)
"""

from anytree import Node, RenderTree
from functools import reduce
from rich.table import Table
from rich.console import Console

from MultiplicativePersistence import MpNumberVariant


class Tree:
    def __init__(self, collection):
        self.collection = collection
        self.node_dict = self.build_node_dict()

    def get_node(self, num):
        """Get the sub tree of the given integer"""
        if num not in self.node_dict:
            raise Exception(f"The number {num} does not appear in this tree")
        return self.node_dict[num]

    def add_child(self, child_num):
        """Given an integer, build the MP chain and integrate it into the trees"""
        mp_list = self.get_mp_list(child_num)
        parent_node = self.get_node(mp_list[0])
        for num in mp_list[1:]:
            if num in self.node_dict:
                parent_node = self.get_node(num)
                continue

            new_node = Node(num, parent=parent_node)
            self.node_dict[num] = new_node

            parent_node = new_node

    def get_max_mp(self, root=None):
        """
        Given the root of the tree, find the maximum MP.
        """
        if root is None:
            return max([self.get_node(i).height for i in range(10)]) + 1
            # Test the roots of all trees
        root_node = self.get_node(root)
        return root_node.height + 1

    def build_node_dict(self):
        """Generate the trees given the provided collection"""
        self.node_dict = {x: Node(x) for x in range(10)}
        variants = self.collection.all_variants()
        for variant in variants:
            self.add_child(variant.base_10)
        return self.node_dict

    @classmethod
    def get_digit_product(self, n):
        """Get the product of all digits of a number"""
        int_list = [int(x) for x in str(n)]
        return reduce((lambda x, y: x * y), int_list)

    @classmethod
    def get_mp_list(self, num):
        """Return the chain of numbers that make up an integer's MP"""
        return_list = [num]
        this_num = num
        while len(str(this_num)) != 1:
            this_num = self.get_digit_product(this_num)
            return_list.append(this_num)
        return list(reversed(return_list))

    def print(self, root=None):
        if root is not None:
            for pre, fill, node in RenderTree(self.get_node(root)):
                Console().print(f"{pre}{node.name}")

    def print_summary(self, root=None):
        """Print a summary of the tree"""
        table = Table(show_footer=False)
        table.add_column("Root", justify="center")
        table.add_column("Max MP", justify="right")
        table.add_column("Descendant Count", justify="right")

        roots = range(10) if root is None else [root]
        for i in roots:
            node = self.get_node(i)
            row = [str(x) for x in [i, self.get_max_mp(root=i), len(node.descendants)]]
            table.add_row(*row)
        Console().print(table)
