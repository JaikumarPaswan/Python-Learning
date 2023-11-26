#include <stdio.h>

void printAdd(int a){  //-> Prototype me bhi define kr skte hai function ko
    printf("The address of variable a is %u\n", &a);
}
int main(){
   int i = 4;
   printf("The value of variable i is %d\n", i);
    printAdd(i); //This is a copy of main i in function printAdd(), Therefore both address will be different
   printf("The address of variable i is %u\n", &i);

    return 0;
}