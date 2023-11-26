#include <stdio.h>
#include <string.h>

struct employee{
    int code;
    float salary;
    char name[10];
};  //---> Semicolon(;)

int main(){
    int a = 34;
    char b = 'g';
    float d = 234.667;
    //employee e1;
    //e1.salary = 34.5454; --->won't work without employee structure

    struct employee e1;
    e1.code = 100;
    e1.salary = 34.4544;
    //e1.name ="Harry"; -->wont work for strings
    strcpy(e1.name, "Harry");

    printf("%d\n", e1.code);
    printf("%.3f\n", e1.salary); //--> only 3 decimal after point will be displayed
    printf("%s\n", e1.name);

    return 0;
}