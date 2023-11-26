#include <stdio.h>

int main(){
    int a,b,c,d;
    printf("Enter the number:\n");
    scanf("%d%d%d%d",&a,&b,&c,&d);

    if(a>b && a>c && a>d){
        printf("%d is greatest number among the following", a);
    }
    else if(b>c && b>d){
        printf("%d is greatest number among the following", b);
    }
    else if(c>d){
        printf("%d is greatest number among the following", c);
    }
    else{
        printf("%d is greatest number among the following", d);
    }
    return 0;
}