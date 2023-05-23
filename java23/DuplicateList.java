package java23;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class DuplicateList {

    public static List<Object> duplicate(List<String> list) {

        List<Object> duplicateList = new ArrayList<>();

        for (int i = 0; i < list.size(); i++) {
            if (i == 0 || (!list.get(i).equals(list.get(i-1)))) {

                duplicateList.add(list.get(i));
            }
        }

        return duplicateList;

    }

    public static void main(String[] args) {

        List<String> exampleList = new ArrayList<>(Arrays.asList("a", "a", "a", "b", "b", "c", "d", "a", "a", "e"));
        

        List<Object> duplicateList = duplicate(exampleList);
        System.out.println(duplicateList);
    }
    
}


