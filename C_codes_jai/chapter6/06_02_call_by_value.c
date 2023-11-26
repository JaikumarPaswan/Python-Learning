#include <stdio.h>
int sum(int a, int b);
int main(){
    int x=3, y=4;
    printf("The value of x and y is %d and %d\n", x, y);
    printf("The value of 3+4 is %d\n", sum(x, y));
    printf("The value of x and y after function call is %d and %d\n", x, y);

    
    return 0;
}
int sum(int a, int b){  //Value of x=3 and y=4 is copied in int a and int b
    int c;
    c = a+b; 
    a=3434;  //Throught function we cannot change the value of variable in Main function, therefore output will be 7
    b=5654;

    return c;
}
