public class solution{
  public int twoSumClosest(int[]nums, int target){
    if (nums == null || nums.length < 2){
      return -1;
    } 
    Array.sort(nums);
    int left=0;
    int right = nums.length - 1;
    int diff = INTEGER.MAX_VALUE;
    while (left < right){
      if( (nums[left] + nums[right]) < target){
        diff = Math.min(diff, target - nums[left] - nums[right]);
        left++
      }else{
        diff = Math.min(diff, nums[left] + nums[right]- target);
        right--
      }
    }
    return diff;
  }
}
