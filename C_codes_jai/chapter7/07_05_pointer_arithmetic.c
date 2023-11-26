// #include <stdio.h>

// int main(){
//     int i = 34;  //int 4 byte ka hai to +1 pr 4 increment hoga
//     int *ptr = &i;
//     printf("The value of ptr is %u\n", ptr);
//     printf("The value of i is %d\n", *ptr);

//     ptr = ptr + 1;
//     ptr++;
//     printf("The value of ptr is %u\n", *ptr);

//     return 0;
// } 


// #include <stdio.h>

// int main(){

//     char i = 'A';   
//     char *ptr = &i; //char 1 byte ka hota hai so 1 hi increment hoga

//     printf("The value of ptr is %u\n", ptr);
//     printf("The value of i is %c\n", *ptr);

//     ptr = ptr + 1;
//     ptr++;
//     printf("The value of ptr is %u\n", ptr);

//     return 0;
// } 

#include <stdio.h>

int main(){

    float i = 7.2;   
    char *ptr = &i; //char 1 byte ka hota hai so 1 hi increment hoga

    printf("The value of ptr is %u\n", ptr);
    printf("The value of i is %f\n", *ptr);

    ptr = ptr + 1;
    ptr++;
    printf("The value of ptr is %u\n", ptr);

    return 0;
} 

