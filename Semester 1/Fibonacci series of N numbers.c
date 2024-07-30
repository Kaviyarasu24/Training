#include<stdio.h>
int main()
{
	int i,n;
	int t1=0,t2=1;
	int nterm=t1+t2;
	printf("n: ");
	scanf("%d",&n);
	printf("%d %d ",t1,t2);
	for(i=3;i<=n;i++){
		printf("%d ",nterm);
	    t1=t2;
		t2=nterm;
		nterm=t1+t2;}
	return 0;
}
