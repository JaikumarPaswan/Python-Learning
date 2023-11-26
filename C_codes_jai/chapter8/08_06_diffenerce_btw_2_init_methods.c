#include <stdio.h>

int main(){
    
    char *ptr = "Harry bhai"; //String defined using pointer can be reinitialized
    //char ptr[] = "Harry bhai"; //String defined suingarray can't be reinitialized
    ptr = "Shubham Bhai";
    
    printf("%s", ptr);
    return 0;
}