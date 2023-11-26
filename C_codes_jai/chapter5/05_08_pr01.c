//write a program using functions to find average of 3 numbers
// #include <stdio.h>
// float average(int a, int b, int c);

// int main(){
//     int a, b, c;
//     printf("Enter value of a\n");
//     scanf("%d", &a);
//     printf("Enter value of b\n");
//     scanf("%d", &b);
//     printf("Enter value of c\n");
//     scanf("%d", &c);
//     printf("The average of 3 number is %f", average(a, b, c));
//     return 0;
// }

// float average(int a, int b, int c){
//     float result;
//     result = (float)(a+b+c)/3;
//     return result;
// }

#include <stdio.h>
float farenheit(int x);
int main(){
    int x;
    printf("Enter Temperature in degree celcius\n");
    scanf("%d", &x);
    printf("temperature in fahrenheit is %f\n", farenheit(x));

    return 0;
}

float farenheit(int x){
    float result;
    result = (float)(x * 9.5) + 32;
    return result;
}

