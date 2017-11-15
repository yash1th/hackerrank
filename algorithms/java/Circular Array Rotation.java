import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    
        
Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int q=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++)
            arr[i]=sc.nextInt();
        int temp=0;
        if(k%n==0);
        else if(k<n && k<n/2){
            k=k%n;
            for(int j=0;j<k;j++) {
                temp = arr[arr.length - 1];
                for (int i = arr.length - 2; i >= 0; i--) {
                    arr[i + 1] = arr[i];
                }
                arr[0] = temp;
            }

        }
        else{
            k=k%n;
            k=n-k;
            for(int j=0;j<k;j++) {
                temp = arr[0];
                for (int i = 1; i < arr.length; i++) {
                    arr[i - 1] = arr[i];
                }
                arr[arr.length-1] = temp;
            }

        }
        int[] index=new int[q];
        for(int i=0;i<q;i++)
            index[i]=sc.nextInt();
        for(int i=0;i<q;i++)
            System.out.println(arr[index[i]]);



    }
}