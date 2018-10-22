
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Sort2 {

    public static void main(String[] args) {
        helper(new int[] {3, 1, 2, 2, 4});
    }

    private static void helper(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int n : arr) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        TreeMap<Integer, List<Integer>> freq = new TreeMap<>();
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            freq.putIfAbsent(entry.getValue(), new ArrayList<>());
            freq.get(entry.getValue()).add(entry.getKey());
        }

        for(Map.Entry<Integer, List<Integer>> entry : freq.entrySet()) {
            List<Integer> list = entry.getValue();
            int times = entry.getKey();
            Collections.sort(list);
            for(int n : list) {
                for(int i = 0; i < times; i++) {
                    System.out.println(n);
                }
            }
        }
    }
}

