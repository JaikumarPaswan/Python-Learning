#include <stdio.h>

int main(){
    char s[2];  //Doubt-> [] k andar ka value kis kam ka hai. koi bhi number dalu to value output me koifarak nah hai
    printf("Enter your name: ");
    scanf("%s", s);
    printf("Your name is %s", s);

    return 0;
}