package google;
 
/**
 * We are given an unsorted array of n distinct elements. Use binary search to find a specific number.
 * Which numbers are guaranteed to be able to be found using binary search in the array?
 * 
 * For example: Given [2,1,3,4,6,5] target = 5, we cannot find 5. Because when
 * the random index is 5, we get element 6, then right pointer will move left,
 * so we'll lose the opportunity to find target 5.
 * 
 * Given [2,1,3,4,5,6] target = 5, we can find 5. Because wherever the random
 * index picks, we'll find target at last.
 * 
 * In [2,1,3,5,4,6], 3 and 6 are the numbers guaranteed to be found.
 * In [1,2,3], all the numbers guaranteed to be found.
 * In [3,2,1], no numbers guaranteed to be found.
 */
public class GuaranteedBinarySearchNumbers {
    public static int findGuranteedBinarySearch(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return nums.length;
        }
        int n = nums.length;
        // nums[i] > any number on its left (leftMax) &&
        // nums[i] < any number on its right (rightMin)
        int[] leftMax = new int[n];
        int left = nums[0];
 
        for (int i = 0; i < n; i++) {
            left = Math.max(left, nums[i]);
            leftMax[i] = left;
        }
 
        int count = 0;
        if (nums[n - 1] > leftMax[n - 2]) {
            count++;
        }
        int right = nums[n - 1];
        for (int i = n - 2; i > 0; i--) {
            if (nums[i] < right && nums[i] > leftMax[i - 1]) {
                count++;
            }
            right = Math.min(right, nums[i]);
        }
 
        if (nums[0] < right) {
            count++;
        }
        return count;
    }
     
    public static void main(String[] args) {
        System.out.println(findGuranteedBinarySearch(new int[] {2,1,3,5,4,6}));
        System.out.println(findGuranteedBinarySearch(new int[] {1,2,3}));
        System.out.println(findGuranteedBinarySearch(new int[] {3,2,1}));
    }
}
