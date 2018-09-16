class Node:
    def __init__(self, name, val, child):
        self.child = child
        self.val = val
        self.name = name

        # self.val_plus_children = val
    average, node = 0, None

    def findSubtree(self, root):
        self.helper(root)
        return self.node.val

    def helper(self,root):
        if root is None:
            return 0,0
        if root.child is None:
            return root.val, 1
        else:
            cur_size = 0
            cur_weight =0
            for child in root.child:
                total_weight, total_size = self.helper(child)
                cur_size += total_size
                cur_weight += total_weight
                # print(cur_weight, cur_size)
            sum, number_tree = cur_weight + root.val, cur_size + 1
            # print(sum, number_tree)

        if self.node is None or sum * 1.0 /number_tree > self.average:
            self.node = root
            self.average = sum * 1.0/ number_tree
        return sum, number_tree


leaf1 = Node('C1', 58, None)
leaf2 = Node('C2', 7, None)
leaf5 = Node('C5', 80, None)

leaf3 = Node('C3', 10, None)
leaf4 = Node('C4', 20, None)
leaf6 = Node('C6', 40, None)

subroot = Node('B1', 150, [leaf1, leaf2, leaf5])
subroot1 = Node('B2', 50, [leaf3, leaf4, leaf6])

root = Node('A', 100, [subroot, subroot1])
# subroot.findSubtree(root)
print(root.findSubtree(root))
