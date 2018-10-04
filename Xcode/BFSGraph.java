package google;
 
import java.util.*;
 
/**
File1:
import File2;
import File3;
 
File2:
import File3;
 
File3：
import File4;
 
File4：
import File1;
 
 */
public class BFSGraph {
 
    Set<String> getTransitivelyImportedFiles(String filename) {
        Queue<String> q = new LinkedList<>();
        q.add(filename);
        Set<String> visited = new HashSet<>();
 
        while (!q.isEmpty()) {
            String cur = q.remove();
            for (String imported : getDirectlyImportedFiles(cur)) {
                if (visited.add(imported)) {
                    q.add(imported);
                }
            }
        }
 
        return visited;
    }
 
    private List<String> getDirectlyImportedFiles(String file) {
        return null;
    }
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
 
    }
 
}
