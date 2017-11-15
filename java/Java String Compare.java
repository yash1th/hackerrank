import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
Scanner sc = new Scanner(System.in);
        String st = sc.next();
        int n = sc.nextInt();
        int i = 0;
        String min=st.substring(i,i+n);
        String max=st.substring(i,i+n);
        while(i+n-1<st.length()){
            //System.out.println("substring = "+st.substring(i,i+n));
            //System.out.println();
            if(st.substring(i,i+n).compareTo(min)<0)
                min=st.substring(i,i+n);
            if(st.substring(i,i+n).compareTo(max)>0)
                max=st.substring(i,i+n);
            ++i;
        }

        System.out.println(min);
        //System.out.println(min.length());
        //System.out.println();
        System.out.println(max);
    }
}