import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
             Scanner sc = new Scanner(System.in);
        int[][] arr = new int[6][6];
        for (int i = 0; i < 6; i++)
            for (int j = 0; j < 6; j++)
                arr[i][j] = sc.nextInt();

        int i = 0, j = 0;
        int max = 0;
        for (i = 0; i < 3; i++) {
            for (j=0; j < 3; j++) {
                max = max + arr[i][j];
            }
        }
        max = max - arr[1][0] - arr[1][2];
        i = 0;
        j = 0;
        int sum = 0;
        while (i <= 3 ) {
            j=0;
            while (j <= 3) {
                for (int a = i; a < i + 3; a++) {
                    for (int b = j; b < j + 3; b++) {
                        sum = sum + arr[a][b];
                    }
                }
                sum = sum - arr[i + 1][j] - arr[i + 1][j + 2];
                if (max < sum) {
                    max = sum;
                }
                sum = 0;
                ++j;
            }
            ++i;
        }
        System.out.println(max);

    }
}
