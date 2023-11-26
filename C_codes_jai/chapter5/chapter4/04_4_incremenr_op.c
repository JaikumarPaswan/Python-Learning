// #include <stdio.h>

// int main(){
//     int i=5;
//     printf("The value of i++ is %d\n", i++); // i++ ---> Pehle print kare fir increment kare

//     printf("The value of i is %d\n", i);

//     printf("The value of ++i is %d\n", ++i); // ++i ---> Pehle increment kare fir print kare

//     return 0;
// }



#include <stdio.h>

int main(){
    int i=5;
    printf("The value of ++i is %d\n", ++i); // ++i ---> Pehle increment kare fir print kare
    i++;
    ++i;

    printf("The value of i is %d\n", i);

    i+=10;  //--> Increment of i by 10

    printf("The value of ++i is %d\n", ++i); // ++i ---> Pehle increment kare fir print kare

    return 0;
}