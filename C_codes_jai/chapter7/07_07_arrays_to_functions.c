// #include <stdio.h>

// void printArray(int *ptr, int n){
//     for(int i=0; i<n; i++){
//         printf("The value of element %d is %d\n",i+1, *(ptr+i));
//     }

// }

// int main(){
//     int arr[]={1,22,52,32,24,68,96};
//     printArray(arr, 7);
//     return 0;
// }

#include <stdio.h>

void printArray(int ptr[], int n){
    for(int i=0; i<n; i++){
        printf("The value of element %d is %d\n",i+1, ptr[i]);
    }

    ptr[2] = 555;//This value will be changes in arr array main as well

}

int main(){
    int arr[]={1,22,52,32,24,68,96};
    printArray(arr, 7);
    printf("%d", arr[2]);

    return 0;
}