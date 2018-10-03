import java.util.HashSet;
import java.util.Stack;
import java.util.Set;

public class Ckeck_log_history {
    static int check_log_history(String[] events){
        if (events == null || events.length == 0){
            return 0;
        }
        int step = 0;
        int len = events.length;
        Stack<Integer> stack = new Stack<>();
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < len; i++){
            step++;
            String cursorStr = events[i];
            int cursorNum = Integer.parseInt(cursorStr.substring(8));
            System.out.println(cursorNum);
            if (cursorStr.charAt(0) == 'A'){
                if (set.add(cursorNum)){
                    stack.push(cursorNum);
                } else {
//                    System.out.println(step);
                    return step;
                }
            } else {
                if (set.remove(cursorNum)){
                    if (stack.pop() != cursorNum){
                        System.out.println(step);
                        return step;
                    }
                } else {
//                    System.out.println(step);
                    return step;
                }
            }
        }
        return stack.size() == 0 ? 0: ++step;
    }
    public static void main(String[] args) {
        String[] events = { "ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364"};
//        String[] events = { "ACQUIRE 364", "ACQUIRE 84", "RELEASE 364", "RELEASE 84"};
//        String[] events = { "ACQUIRE 123", "ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364", "ACQUIRE 456"};
//        String[] events = { "ACQUIRE 364", "ACQUIRE 84", "ACQUIRE 84", "RELEASE 364"};
//        String[] events = { "ACQUIRE 123", "ACQUIRE 364", "ACQUIRE 84", "RELEASE 84", "RELEASE 364", "ACQUIRE 789", "RELEASE 456", "RELEASE 123"};
        System.out.println(check_log_history(events));
    }
}
