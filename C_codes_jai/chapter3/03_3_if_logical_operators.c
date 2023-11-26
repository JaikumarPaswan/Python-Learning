#include <stdio.h>

int main()
{
    int age;
    int vipPass = 1;  //Now anyone can drive

    printf("Enter your age\n");
    scanf("%d", &age);

    if ((age <= 70 && age >= 18) || (vipPass==1)) //logical operator AND , OR
    
    {
        printf("You can drive\n");
    }

    else
    {
        printf("You cannot drive\n");
    }
    return 0;
}