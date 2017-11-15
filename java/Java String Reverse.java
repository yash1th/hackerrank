import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        
        int i=A.length()-1;
        String rev="";
        while(i>=0){
            rev+=A.charAt(i);
            --i;
        }
        if(A.equals(rev)){
            System.out.println("Yes");
        }
        else
            System.out.println("No");

        
    }
}