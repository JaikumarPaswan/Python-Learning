#include <stdio.h>

int main()
{
    int rating;
    printf("Enter your rating (1-5)\n");
    scanf("%d", &rating);

    switch (rating)
    {
    case 1:
        printf("Your rating is 1\n");
        break; //its will help to execute the perticular statement (agar nahi use kiya to jis point par value satisfy hoga vaha se niche ka sara printf display krdega)
    case 2:
        printf("Your rating is 2\n");
        break;
    case 3:
        printf("Your rating is 3\n");
        break;
    case 4:
        printf("Your rating is 4\n");
        break;
    case 5:
        printf("Your rating is 5\n");
        break;
    default:
        printf("Invalid rating\n");
        break;
    }
    return 0;
}