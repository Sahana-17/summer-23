//Problem 5

package java23;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Main
{
    public static void main(String[] args)
    {
        List<String> list = new ArrayList<>(Arrays.asList("a", "b", "c", "d", "e"));
 
        for (int i = 0, j = list.size() - 1; i < j; i++) {
            list.add(i, list.remove(j));
        }
 
        System.out.println(list);
    }
}
