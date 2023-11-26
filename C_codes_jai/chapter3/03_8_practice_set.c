#include <stdio.h>

int main(){
    int Physics, Chemistry, Maths;
    float total;
    printf("Enter your Physics marks\n");
    scanf("%d", &Physics);

    printf("Enter your Chemistry marks\n");
    scanf("%d", &Chemistry);

    printf("Enter your Maths marks\n");
    scanf("%d", &Maths);

    total=(Physics + Chemistry + Maths)/3;


    if(total<40 || Physics<33 || Chemistry<33 || Maths<33)
    {
        printf("Your total percentege is %f and you are failed", total);
    }
    else
    {
        printf("Your total percentege is %f and you are Passed", total);
    }

    return 0;
}