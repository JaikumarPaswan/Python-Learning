#include <stdio.h>
// Compiler ko bataya ki-> sum is a function which takes a and b as an input and returns an integer as an output
int sum(int a, int b);  // fuction prototype declaration

int main(){
    int c;
    c = sum(2,6); // function call  //Here, 2 & 6 are arguments
    printf("The value of c is %d\n", c);
    return 0;
}

int sum(int a, int b){  //function definition //Here,a & b are parameters
    int c;  // ye c aur main function vale c me koi relation nhi hai
    c = a + b;
    return c;
}