import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int arr[] = new int[n];
        for(int arr_i=0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        int neg=0,pos=0,zer=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]<0)
                ++neg;
            else if(arr[i]==0)
                  ++zer;
            else
                ++pos;
           }
        System.out.println((double)pos/arr.length);
        System.out.println((double)neg/arr.length);
        System.out.println((double)zer/arr.length);


    }
}
