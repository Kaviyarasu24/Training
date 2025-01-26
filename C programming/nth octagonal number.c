#include<stdio.h>
int main()
{
	int n,value;
	printf("Enter a number : ");
	scanf("%d",&n);
	if(n>0){
	value=(3*n*n-2*n);
	printf("%d\n",value);}
    else{
		printf("Invalid input\n");
	}
	return 0;
}
