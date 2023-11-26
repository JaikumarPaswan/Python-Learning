#include <stdio.h>

int main(){
    //char str[] = "Harry"; //-> In such case, '\0' will be appended at the end of the string by the compiler.
    char str[] = {'H', 'a', 'r', 'r', 'y', '\0'};
    char *ptr = str;
    while(*ptr!= '\0'){
        printf("%c", *ptr);
        ptr++;
    }
    return 0;
}