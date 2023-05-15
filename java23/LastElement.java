//Day1

package java23;
import java.util.List;

public class LastElement {
    public static void main(String[] args) {
        List<String> list = List.of("a", "b", "c", "d");

        if (list.isEmpty()) {
            System.out.println("Empty List");
        } else {
            String lastElement = list.get(list.size() - 1);
            System.out.println("Last Element: " + lastElement);

        }
        
    }
}
