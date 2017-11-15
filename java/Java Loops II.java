import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
            Scanner scan = new Scanner(System.in);
        int t;
        t=scan.nextInt();
        int[][] arr=new int[t][3];
        for(int i=0;i<arr.length;i++) {
            for (int j = 0; j < 3; j++) {
                arr[i][j] = scan.nextInt();
            }
        }
        int tempn=0;
        int sum=0;
        int powtotal=0;
        for(int i=0;i<arr.length;i++){
            int n=arr[i][2];
            sum=arr[i][0]+arr[i][1];
            for(tempn=1;tempn<n+1;tempn++) {
                System.out.printf("%d ",sum);
                powtotal = (int) Math.pow(2, tempn);
                sum = sum + powtotal * arr[i][1];
            }
            System.out.println();
        }
    }
}