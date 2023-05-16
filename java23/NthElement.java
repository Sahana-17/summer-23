//Problem3

package java23;
import java.util.List;
import java.util.Scanner;

public class NthElement {
    public static void main(String[] args) {
        List<String> list = List.of("a", "b", "c", "d", "e");

        Scanner num = new Scanner(System.in);
        System.out.print("Enter n : ");
        int n = num.nextInt();

        if (list.isEmpty()) {
            System.out.println("Empty List");
        } else {
            String nthElement = list.get(n - 1);
            System.out.println("Element : " + nthElement);
        }
    }
    
}


