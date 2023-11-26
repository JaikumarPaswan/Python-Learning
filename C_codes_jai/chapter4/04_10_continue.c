#include <stdio.h>

int main(){
    int skip=5, i=0;
    while(i<10){
        i++;
        if(i!=skip){  //5 nahi aya to skip/continue kro, jaise hi 5 ayaa to execute kro
            continue;
        }
    else{
        printf("%d\n",i);
        }
    }
    return 0;
}