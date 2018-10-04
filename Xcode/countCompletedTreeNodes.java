package google;
 
 
    /**
     * Count Complete Tree Nodes 
     * Given a complete binary tree, count the number of nodes
     */
    public int countNodes(TreeNode root) {
        return countNodes(root, -1, -1);
    }
 
    public int countNodes(TreeNode node, int leftHeight, int rightHeight) {
        if (node == null) {
            return 0;
        }
 
        TreeNode tmp = node.left;
        if (leftHeight == -1) {
            leftHeight = 0;
            while (tmp != null) {
                leftHeight++;
                tmp = tmp.left;
            }
        }
 
        tmp = node.right;
        if (rightHeight == -1) {
            rightHeight = 0;
            while (tmp != null) {
                rightHeight++;
                tmp = tmp.right;
            }
        }
 
        if (leftHeight == rightHeight) {
            // found complete tree
            return (1 << (leftHeight + 1)) - 1; // 2^(leftHeight + 1) - 1
        }
 
        return 1 + countNodes(node.left, leftHeight - 1, -1) + countNodes(node.right, -1, rightHeight - 1);
    }
