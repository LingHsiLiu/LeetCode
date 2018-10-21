import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
 
public class AlternatingParityPermutation {
 
    public static void main(String[] args) {
        System.out.println(permute(new int[] {1, 2, 3 ,4}));
    }
     
    public static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), nums, 0, new HashSet<>(), null);
        return res;
    }
     
    public static void backtrack(List<List<Integer>> res, List<Integer> path, int[] nums, int idx, HashSet<Integer> visit, Integer pre){
        if(path.size() == nums.length){
            res.add(new ArrayList<>(path));
            return;
        }
         
        for(int i = 0; i < nums.length; i++){
            if(!visit.contains(nums[i]) && (pre == null || pre != null && ((pre % 2 == 0) ^ (nums[i] % 2 == 0)))){
                path.add(nums[i]);
                visit.add(nums[i]);
                backtrack(res, path, nums, i + 1, visit, nums[i]);
                visit.remove(nums[i]);
                path.remove(path.size() - 1);
            }
        }
    }
 
}
