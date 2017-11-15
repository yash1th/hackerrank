import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        String[] arr1=new String[sc.nextInt()];
        for(int i=0;i<arr1.length;i++)
            arr1[i]=sc.next();
        String[] arr2=new String[sc.nextInt()];
        for(int i=0;i<arr2.length;i++)
            arr2[i]=sc.next();
        for(int i=0;i<arr2.length;i++){
            int total=0;
            for(int j=0;j<arr1.length;j++){
                if(arr2[i].equals(arr1[j]))
                    ++total;
            }
            System.out.println(total);
        }
    
        
    }
}