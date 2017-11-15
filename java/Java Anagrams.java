import java.io.*;
import java.util.*;

public class Solution {

    static boolean isAnagram(String a, String b) {
        
        // Complete the function by writing your code here.
        a=a.toLowerCase();
        b=b.toLowerCase();
        char[] word1=a.replaceAll("[\\s]","").toCharArray();
        char[] word2=b.replaceAll("[\\s]","").toCharArray();
        Arrays.sort(word1);
        Arrays.sort(word2);
        return Arrays.equals(word1,word2);
        
    }
  
    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}