def findDist(bstDistance, node1, node2):
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left, self.right = None, None

    def LCA(root, node1, node2):
        if node1 > node2:
            return LCA(root, node2, node1)
        while True:
            if node1 > root.val:
                root = root.right
            else:
                root = root.left
            if node1 <= root.val and node2 >= root.val:
                return root

    def Cal_Dist(root, node):
        ret = 0
        while root.val != node:
            if node > root.val:
                root = root.right
            else:
                root = root.left
            ret += 1
        return ret

    if node1 == node2 or len(bstDistance) == 0:
        return 0
    root = TreeNode(bstDistance[0])
    for i in range(1, len(bstDistance)):
        node = root
        while node != bstDistance[len(bstDistance)-1]:
            # print(bstDistance[i])
            if bstDistance[i] > node.val:
                if not node.right:
                    node.right = TreeNode(bstDistance[i])
                    break
                node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(bstDistance[i])
                    break
                node = node.left

    node = LCA(root, node1, node2)
    print(node.val)
    dist1 = Cal_Dist(node, node1)
    dist2 = Cal_Dist(node, node2)
    print(dist1 + dist2)
    return dist1+ dist2

bstDistance = [2, 0, 3, 5, 6, 4, 7, 8, 1]
node1 = 7
node2 = 4
print(findDist(bstDistance, node1, node2))
