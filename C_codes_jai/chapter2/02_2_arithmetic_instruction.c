#include <stdio.h>
#include <math.h>

int main()
{
    int a = 4;
    int b = 8;
    int z = b * a; //we cant write b*a=z->(illegal)
    printf("The value of a+b is:%d\n", a + b);
    printf("The value of a-b is:%d\n", a - b);
    printf("The value of a*b is:%d\n", a * b);
    printf("The value of a/b is:%d\n", a / b);

    printf("The value of z is:%d\n", z);

    printf("5 when divided by 2 leaves a remainder of %d\n", 5 % 2); //(%) is a modular division operator
                                                                     //which can give the remainder.
    printf("-5 when divided by 2 leaves a remainder of %d\n", -5 % 2);
    printf("5 when divided by -2 leaves a remainder of %d\n", 5 % -2);

    //printf("The value of 4*5 is %d/n", (4)(5)); -> This is invalid as proper
    //sign is required of operator

    printf("The value of 4 to the power 5 is %f\n", pow(2,5));                

    //printf("The value of 4^5 is %d/n", 4^5); -> will not produce 4 to the power 5                                           
    return 0;
}