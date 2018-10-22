//        int[] input = new int[]{8,5,5,5,5,1,1,3,3,4};
//        output = 4,8,1,1,3,3,5,5,5,5


import java.util.Comparator;
import java.util.HashMap;
import java.util.Arrays;

public class Sort {

    public static void main(String[] args) {
//        int n = 10;
//        int[] input = new int[]{8,5,5,5,5,1,1,3,3,4};
        int[] input = new int[]{4,5,6,5,4,3};
        int n = input.length;

        HashMap<Integer, Integer> map = new HashMap<>();
        Integer[] nums = new Integer[n];
        for (int i = 0; i < n; i++) {
            nums[i] = new Integer(input[i]);
            System.out.println(nums);
            map.put(input[i], map.getOrDefault(input[i], 0) + 1);
            System.out.println(map);
        }

        Arrays.sort(nums, new Comparator<Integer>(){
            public int compare(Integer o1, Integer o2) {
                Integer c1 = map.get(o1);
                Integer c2 = map.get(o2);
                if (c1 != c2) {
                    return Integer.compare(c1, c2);
                }
                else {
                    return Integer.compare(o1, o2);
                }
            }
        });
        for (Integer num : nums) {
            System.out.println(num);
        }
    }
}
