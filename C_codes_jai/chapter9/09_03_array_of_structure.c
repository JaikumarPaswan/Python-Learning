#include <stdio.h>
#include <string.h>

struct employee{
    int code;
    float salary;
    char name[10];
};

int main(){
    struct employee facebook[100];
    facebook[0].code = 100;
    facebook[0].salary = 100.45;
    strcpy(facebook[0].name, "Jai");

    facebook[1].code = 101;
    facebook[1].salary = 100.45;
    strcpy(facebook[1].name, "Raj");

    facebook[2].code = 102;
    facebook[2].salary = 100.45;
    strcpy(facebook[2].name, "Chetan");

    printf("%d\n", facebook[0].code);
    printf("%.3f\n", facebook[0].salary); 
    printf("%s\n", facebook[0].name);
    return 0;
}