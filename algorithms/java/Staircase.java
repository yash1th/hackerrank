import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int spaces=n-1;
        
        int temp1=spaces;
        int temp2=1;
        while(temp2<=n){
            temp1=spaces;
            while(temp1>0){
                System.out.print(" ");
                --temp1;
            }
            --spaces;
            int i=0;
            while(i<temp2){
                System.out.print("#");
                ++i;
            }
            ++temp2;
            System.out.println();  
        }
    }
}
