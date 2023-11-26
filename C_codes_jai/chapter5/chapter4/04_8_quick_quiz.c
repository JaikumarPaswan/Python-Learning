#include <stdio.h>

int main(){
   
   int  n;
   printf("Enter the value of n\n");
   scanf("%d",&n);

   for(int i=n; i; i--)
       printf("Value of first N natural numbers is:%d\n", i);
   
    return 0;
}
   