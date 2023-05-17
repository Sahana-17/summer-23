//Problem 4

package java23;

import java.util.List;

public class NoofElements {
    
    public static void main(String[] args) {
        List<String> list = List.of("a", "b", "c", "d", "e");

        if (list.isEmpty()) {
            System.out.println("Empty List");
        } else {
            int noofelements = list.size();
            System.out.println("No of Elements : " + noofelements);
        }
    }
    
}


