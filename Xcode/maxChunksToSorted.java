    /**
     * Max Chunks To Make Sorted
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
 
What is the most number of chunks we could have made?
 
Example 1:
 
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:
 
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
Note:
 
arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
     */
    public int maxChunksToSorted(int[] arr) {
        int ans = 0, max = 0;
        for (int i = 0; i < arr.length; ++i) {
            max = Math.max(max, arr[i]);
            if (max == i) {
                ans++;
            }
        }
        return ans;
    }
 
    /**
     * Max Chunks To Make Sorted II
This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.
 
Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
 
What is the most number of chunks we could have made?
 
Example 1:
 
Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:
 
Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
Note:
 
arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].
     */
    public int maxChunksToSorted2(int[] arr) {
        // Key is number, Value is its occurrence
        Map<Integer, Integer> count = new HashMap<>();
        int ans = 0, diff = 0;
 
        int[] expect = arr.clone();
        Arrays.sort(expect);
 
        for (int i = 0; i < arr.length; ++i) {
            int x = arr[i], y = expect[i];
 
            int xCount = count.getOrDefault(x, 0) + 1;
            count.put(x, xCount);
            if (xCount == 0) {
                diff--;
            }
            if (xCount == 1) {
                diff++;
            }
 
            int yCount = count.getOrDefault(y, 0) - 1;
            count.put(y, yCount);
            if (yCount == -1) {
                diff++;
            }
            if (yCount == 0) {
                diff--;
            }
 
            if (diff == 0) {
                ans++;
                count.clear();
            }
        }
 
        return ans;
    }
