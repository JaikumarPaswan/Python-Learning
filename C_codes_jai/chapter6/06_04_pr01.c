#include <stdio.h>

int main(){
    int a = 6;
    int *ptr = &a;  //One Line pointer and its value //*ptr stores the value present at the address of 'a'
    //ptr = &a;
    printf("The address of a is %u\n", &a);
    printf("The value of variable a is %d\n", a);
    printf("The value of variable a is %d\n", *ptr);
    printf("The address of variable a is %u\n", ptr);
    return 0;
}