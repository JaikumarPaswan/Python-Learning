#include <stdio.h>
#include<string.h>

int main(){
    char st1[45] = "Hello";
    char *st2 = "Jai";
    int val = strcmp(st1, st2); //ASCI value of first mis-matching character st1-st2
    printf("Now the val is %d", val);
    return 0;
}