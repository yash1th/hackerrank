import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int k = in.nextInt();
            int a[] = new int[n];
            for(int a_i=0; a_i < n; a_i++){
                a[a_i] = in.nextInt();
            }
            int i=0,a_i=0;
            boolean flag=false;
            while(a_i<a.length){
                if(a[a_i]<=0)
                    ++i;
                if(i>=k){
                    flag=true;
                    break;
                }
                ++a_i;
            }
            if(flag)
                System.out.println("NO");
            else
                System.out.println("YES");
        }
    }
}