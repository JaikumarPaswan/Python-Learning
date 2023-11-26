#include <stdio.h>
#include<stdlib.h>

struct node {
	int info;
	struct node* link;
};
struct node* start = NULL;

void insertatStart()
{
	int data;
	struct node* temp;
	temp = malloc(sizeof(struct node));
	printf("\nADD what you want  to"
		" be inserted : ");
	scanf("%d", &data);
	temp->info = data;

	temp->link = start;
	start = temp;
}


void deletionStarting()
{
	struct node* temp;
	if (start == NULL)
		printf("\nList is empty!!!!\n");
	else {
		temp = start;
		start = start->link;
		free(temp);
	}
}

void traverse()
{
    struct node* temp;
 
    
    if (start == NULL)
        printf("\nList is empty!!!!!\n");
 
    
    else {
        temp = start;
        while (temp != NULL) {
            printf("List = %d\n",
                   temp->info);
            temp = temp->link;
        }
    }
}


int main()
{
	int choice;
	while (1) {

		printf("\n\t1 To see the full list\n");
		printf("\t2 For insertion inside the list \n");
		printf("\t3 For deletion of "
			"first element inside the list\n");
		
		printf("\nEnter Choice :\n");
		scanf("%d", &choice);

		switch (choice) {
		case 1:
			traverse();
			break;
		case 2:
			insertatStart();
			break;
		case 3:
			deletionStarting();
			break;
		default:
			printf("Your  Choice in incorrect\n");
		}
	}
	return 0;
}