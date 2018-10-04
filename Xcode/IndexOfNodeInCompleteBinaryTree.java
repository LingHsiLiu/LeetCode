package google;
 
import java.util.*;
 
public class IndexOfNodeInCompleteBinaryTree {
 
    private static class TreeNode  {
        int val;
        TreeNode left;
        TreeNode right;
    }
     
    /**
Given complete binary tree of n nodes sequentially numbered from 0 to n - 1.
The root is 0. Find if an index exists as corresponding tree node in the tree.
     */
    public static boolean doesIndexOfNodeInCompleteBinaryTreeExist(TreeNode root, int index) {
        if (index == 0) {
            return root != null;
        }
        LinkedList<Boolean> track = findTrack(index);
        TreeNode cur = root;
        while (cur != null) {
            boolean dir = track.removeLast();
            if (dir) {
                cur = cur.left;
            } else {
                cur = cur.right;
            }
        }
 
        return cur != null;
    }
     
    /**
     * parent index = (left child index - 1) / 2
     * parent index = right child index / 2 - 1
     * 
     * Use true to represent left, false for right
     */
    private static LinkedList<Boolean> findTrack(int index) {
        LinkedList<Boolean> track = new LinkedList<>();
        while (index != 0) {
            if (index % 2 == 0) {
                // even, right child
                index /= 2;
                index--;
                track.add(false);
            } else {
                // odd, left child
                index--;
                index /= 2;
                track.add(true);
            }
        }
        return track;
    }
 
    public static void main(String[] args) {
        for (int i = 0; i < 15; i++) {
            List<Boolean> l = findTrack(i);
            Collections.reverse(l);
            System.out.println(i + ": " + l);
        }
    }
 
}
