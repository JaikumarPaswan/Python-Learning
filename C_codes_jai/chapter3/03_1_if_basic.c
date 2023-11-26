#include <stdio.h>

int main()
{
    int a;
    printf("Enter a number\n");
    scanf("%d", &a);

    if (a % 2 == 0)
    {
        printf("%d is a Even number\n", a);  //%d hai start me issiliye end me ,(a) dala hai
    }

    else
    {
        printf("%d is a Odd number\n", a);
    }
    
    return 0;
}