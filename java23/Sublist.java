package java23;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Sublist {
    public static List<List<String>> sublist(List<String> list) {
        List<List<String>> newList = new ArrayList<>();
        List<String> sublist = new ArrayList<>();

        for (int i = 0; i < list.size(); i++) {
            if (i == 0 || !list.get(i).equals(list.get(i - 1)) ) {
                if (!sublist.isEmpty()) {
                    newList.add(sublist);
                }
                sublist = new ArrayList<>();
            }
            sublist.add(list.get(i));
        }

        if (!sublist.isEmpty()) {
            newList.add(sublist);
        }

        return newList;
    }

    public static void main(String[] args) {

        List<String> exampleList = new ArrayList<>(Arrays.asList("a", "a", "a", "b", "b", "c", "d", "a", "a", "e"));
        List<List<String>> finalList = sublist(exampleList);
        System.out.println(finalList);
    }
    
}

