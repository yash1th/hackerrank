import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr=new int[sc.nextInt()];
        for(int i=0;i<arr.length;i++)
            arr[i]=sc.nextInt();
        Arrays.sort(arr);
        int updatedIndex=0;
        System.out.println(arr.length);
        for(int i=1;i<arr.length;i++){
            if(arr[updatedIndex]==arr[i]) 
                updatedIndex = i;
            else{
                    System.out.println(arr.length-updatedIndex-1);
                    if(updatedIndex+1>arr.length)
                        break;
                    ++updatedIndex;

                 }

            }
            
    }
}
