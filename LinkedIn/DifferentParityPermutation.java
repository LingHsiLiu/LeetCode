//排列組合
import java.util.Comparator;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;

public class DifferentParityPermutation {
    private static void dfs(int n, List<List<Integer>> lists, List<Integer> cur) {
        if (cur.size() == n) {
            List<Integer> list = new ArrayList<>(cur);
            lists.add(list);
        }
        for (int i = 1; i <= n; i++) { if (cur.contains(i)) {
            continue;
        }
            if (cur.size() > 0) {
                if ((cur.get(cur.size() - 1) % 2) + (i % 2) != 1) {
                    continue;
                }
            }
            cur.add(i);
            dfs(n, lists, cur);
            cur.remove(cur.size() - 1);
        }
    }

    public static void main(String[] args) {
        int n = 5;
        List<List<Integer>> lists = new ArrayList<>();
        if (n == 0) {
            System.out.println("null");
        }
        dfs(n, lists, new ArrayList<Integer>());
        for (List<Integer> innerList : lists) {
            System.out.println(innerList);
        }
    }
}
