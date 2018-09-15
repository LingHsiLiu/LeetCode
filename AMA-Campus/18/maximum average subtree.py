class Node:
    def __init__(self, name, val, child):
        self.child = child
        self.val = val
        self.name = name
        self.val_plus_children = val

    average, node = 0, None
    def findSubtree(self, root):
        self.helper(root)
        print(self.node.val)
        return self.node

    def helper(self, root):
        if root is None:
            return 0, 0
        if root.child is None:
            return root.val, 1
        else:
            cur_size = 0
            cur_weight = 0
            for child in root.child:
                weight, total_node = self.helper(child)
                cur_size += total_node
                cur_weight += weight
                print(cur_weight, cur_size)

            sum, size = cur_weight + root.val, cur_size + 1
            print(sum, size)

        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size
            #print(self.average)
            #print("node")
            #print(self.node.val)

        return sum, size

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
# print(root.get_all_weight(root))
# print
# print(subroot1.get_all_weight())
# print
# print(root.get_all_weight())
