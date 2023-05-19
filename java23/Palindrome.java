//Problem 6

package java23;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Palindrome {

    public static boolean isPalindrome(List<String> list) {

        for (int i = 0; i < list.size() / 2; i++) {
            if (!list.get(i).equals(list.get(list.size() - i - 1))) {
                return false;
            }
        }
        return true;

    }

    public static void main(String[] args) {

        List<String> list = new ArrayList<>(Arrays.asList("a", "b", "c", "b", "a"));
        boolean check_palindrome = isPalindrome(list);

        if (check_palindrome == true) {
            System.out.println("Palindrome");
        } else {
            System.out.println("Not Palindrome");
        }
    }
}