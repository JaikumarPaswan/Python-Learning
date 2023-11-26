#include <stdio.h>
void change(int a);

int main(){
    int b = 344;
    printf("The value of b before change is %d\n",b);
    change(b);
    printf("The value of b after change is %d\n",b);  //in output we can see that change is just a name of function and not a propertie so no actual change is seen
    return 0;
}

void change(int a){
    a = 77;
}