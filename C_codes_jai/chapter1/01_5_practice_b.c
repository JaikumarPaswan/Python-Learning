// #include <stdio.h>

// int main(){
//     int radius=3;
//     float pi=3.14;

//     printf("The area of thos circle is %f\n", pi*radius*radius);

//     int height=4;
//     printf("The volume of this cylinder is %f", pi*height*radius*radius);

//     return 0;
// }


#include <stdio.h>     //with scanf function

int main(){
    int radius;
    float pi=3.14;
    int height;

    printf("Enter value of radius\n");
    scanf("%d", &radius);
    printf("The area of the circle is %f\n", pi*radius*radius);

    printf("Enter the value of height\n");
    scanf("%d", &height);
    printf("Enter the value of radius\n");
    scanf("%d", &radius);
    printf("The volume of this cylinder is %f", pi*height*radius*radius);
    return 0;
}

