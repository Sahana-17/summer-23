//Problem 2

package java23;
import java.util.List;

public class SecondLastElement {
    public static void main(String[] args) {
        List<String> list = List.of("a", "b", "c", "d", "e");

        if (list.isEmpty()) {
            System.out.println("Empty List");
        } else {
            String secondlastElement = list.get(list.size() - 2);
            System.out.println("Second Last Element : " + secondlastElement);
        }
    }
    
}

