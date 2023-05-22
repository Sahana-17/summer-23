package java23;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FlattenList {

    public static List<Object> flatten(List<Object> nestedList) {
        List<Object> flattenedList = new ArrayList<>();

        for (Object item : nestedList) {
            if (item instanceof List) {
                flattenedList.addAll(flatten((List<Object>) item));
            } else {
                flattenedList.add(item);
            }
        }

        return flattenedList;
    }

    public static void main(String[] args) {
        List<Object> nestedList = Arrays.asList("a",
                Arrays.asList("b", "c", Arrays.asList("d", "e")),
                "f",
                Arrays.asList("g", Arrays.asList("h", "i", "j"))
        );

        List<Object> flattenedList = flatten(nestedList);
        System.out.println(flattenedList);
    }
}
