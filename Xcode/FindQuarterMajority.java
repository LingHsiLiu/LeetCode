    /**
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/4 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
     */
public class FindQuarterMajority {
    public static void main(String[] args) {
        int[] nums1 = { 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7 };
        int[] nums2 = { 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7 };
        int[] nums3 = { 1, 1, 2, 2, 3, 3, 4, 5, 7, 7, 7 };
        int[] nums4 = { 1, 2, 3, 3 };
        int[] nums5 = { 1, 1, 2, 3 };
        int[] nums6 = { 1, 2, 2, 2, 3, 3, 4, 5, 7, 7, 7 };
        if (findMajority(nums1) != 3) {
            System.out.println("Wrong Answer! ");
        }
        if (findMajority(nums2) != 3) {
            System.out.println("Wrong Answer! ");
        }
        if (findMajority(nums3) != 7) {
            System.out.println("Wrong Answer! ");
        }
        if (findMajority(nums4) != 3) {
            System.out.println("Wrong Answer! ");
        }
        if (findMajority(nums5) != 1) {
            System.out.println("Wrong Answer! ");
        }
        if (findMajority(nums6) != 2) {
            System.out.println("Wrong Answer! ");
        }
        System.out.println("Accepted! ");
    }
 
    public static int findMajority(int[] arr) {
        if (arr == null || arr.length == 0) {
            throw new NullPointerException();
        }
        int base = arr.length / 4;
        for (int index = base; index < arr.length; index += base) {
            if (findLast(arr, index, arr.length - 1, arr[index]) - 
                    findFirst(arr, 0, index, arr[index]) + 1 > base) {
                return arr[index];
            }
        }
        throw new IllegalArgumentException("Not Found");
    }
 
    private static int findFirst(int[] nums, int start, int end, int target) {
        // find first occurrence of target in range [left, right], return index
        int result = -1;
        while (start <= end && nums[start] <= target && target <= nums[end]) {
            if (nums[start] == target) {
                return start;
            }
            int mid = start + ((end - start) >>> 1);
            if (nums[mid] == target) {
                end = mid - 1;
                result = mid;
            } else if (nums[mid] > target)
                end = mid - 1;
            else {
                start = mid + 1;
            }
        }
        return result;
    }
 
    private static int findLast(int[] nums, int start, int end, int target) {
        // find last occurrence of target in range [left, right], return index
        int result = -1;
        while (start <= end && nums[start] <= target && target <= nums[end]) {
            if (nums[end] == target) {
                return end;
            }
            int mid = start + ((end - start) >>> 1);
            if (nums[mid] == target) {
                start = mid + 1;
                result = mid;
            } else if (nums[mid] > target)
                end = mid - 1;
            else {
                start = mid + 1;
            }
        }
        return result;
    }
}
