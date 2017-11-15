import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[][] = new int[n][n];
        for(int a_i=0; a_i < n; a_i++){
            for(int a_j=0; a_j < n; a_j++){
                a[a_i][a_j] = in.nextInt();
            }
        }
        int sum1=0,sum2=0;
        int i=0,j=0;
        for(;i<n&&j<n;i++,j++)
                sum1+=a[i][j];
        i=0;j=n-1;
        for(;i<n&&j>=0;i++,j--)
                sum2+=a[i][j];
        if((sum1-sum2)<0)
            System.out.println(-(sum1-sum2));
        else
            System.out.println((sum1-sum2));

    }
}
