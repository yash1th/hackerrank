import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a0 = in.nextInt();
        int a1 = in.nextInt();
        int a2 = in.nextInt();
        int b0 = in.nextInt();
        int b1 = in.nextInt();
        int b2 = in.nextInt();
        int at=0,bt=0;
        if(a0>b0)
            ++at;
        else if(a0==b0);
        else
            ++bt;
        if(a1>b1)
            ++at;
        else if(a1==b1);
        else
            ++bt;
            
        if(a2>b2)
            ++at;
        else if(a2==b2);
        else
            ++bt;
            
        System.out.println(at+" "+bt);    
    }
}
