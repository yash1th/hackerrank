#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
       scanf("%i",&arr[i]);
    for(int i=n-1;i>=0;i--)
       printf("%i ",arr[i]);
    return 0;
}