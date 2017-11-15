import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {

Scanner sc=new Scanner(System.in);
            String time=sc.next();
            String[] timeArray=time.split(":");
            int hours=Integer.parseInt(timeArray[0].trim());
            timeArray[2]=timeArray[2].substring(0,2);
            if(time.indexOf("AM")>0){
                if(timeArray[0].equals("12"))
                    System.out.println("00:"+timeArray[1]+":"+timeArray[2]);
                else
                System.out.println(timeArray[0]+":"+timeArray[1]+":"+timeArray[2]);
            }
            else {
                if(timeArray[0].equals("12"))
                    System.out.println("12:"+timeArray[1]+":"+timeArray[2]);
                else
                    System.out.println((hours+12)+":"+timeArray[1]+":"+timeArray[2]);
            }


        
    }
}
