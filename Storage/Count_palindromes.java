import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;

//Purstorage company

public class Count_palindromes {
    static int count_palindromes(String S){
        if (S == null || S.length() == 0){
            return 0;
        }
        int count = 0;
        int len = S.length();
        boolean[][] record = new boolean[len][len];
        for (int i = 0; i < len; i++){
            record[i][i] = true;
//            System.out.println(record[i][i]);
        }
        count += len;
//        System.out.println(count);
        for (int i = 0; i < len -1; i++){
            if (S.charAt(i) == S.charAt(i + 1)){
//                System.out.println(S.charAt(i));
//                System.out.println(S.charAt(i + 1));
//                System.out.println(i);
//                System.out.println(i+1);
                record[i][i+1] = true;
                count++;
//                System.out.println(count);
            }
        }
        for (int i = len - 3; i >= 0; i--){
            for (int j = i + 2; j < len; j++){
                if (record[i + 1][j-1]&& S.charAt(i) == S.charAt(j)){
                    record[i][j] = true;
//                    System.out.println(S.charAt(i));
//                    System.out.println(S.charAt(j));
//                    System.out.println(i);
//                    System.out.println(j);
                    count ++;
//                    System.out.println(count);
                }
            }
        }
        return count;
    }
    public static void main(String[] args) {
//        String S = "ASANtaLivedAsAdeviLatNASA";
        String S = "hellolle";
//        String S = "wowpurerocks";
        System.out.println(count_palindromes(S));
    }
}
