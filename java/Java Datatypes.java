import java.util.*;
import java.io.*;



class Solution{
    public static void main(String []argh)
    {

        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                long x=sc.nextLong();
                long z=(long)Math.pow(2,31);
                long y=(long)Math.pow(2,63);
                //System.out.println(y);
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127)
                    System.out.println("* byte");
                if(x>=-32768&&x<=32767)
                    System.out.println("* short");
                if(x>=(-1*z)&&x<=z-1)
                        System.out.println("* int");
                System.out.println("* long");
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        
        }
    }
}