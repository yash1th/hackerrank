import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();
        StringTokenizer stk=new StringTokenizer(s,"[ !,?._'@]+");
        System.out.println(stk.countTokens());
        while(stk.hasMoreTokens())
        {
            System.out.println(stk.nextToken());
        }

        // Write your code here.
    }
}