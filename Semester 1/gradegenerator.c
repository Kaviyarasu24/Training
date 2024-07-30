#include<stdio.h>
int main()
{
	int m1,m2,m3,total,avg;
	scanf("%d",&m1);
	scanf("%d",&m2);
	scanf("%d",&m3);
	total=m1+m2+m3;
    avg=total/3;
	if(avg>=90)
		printf("The grade is A\n");
	else if(avg>80&&avg<90)
		printf("The grade is B\n");
	else if(avg>70&&avg<=80)
		printf("The grade is C\n");
	else if(avg>60&&avg<=70)
		printf("The grade is D\n");
	else if(avg>50&&avg<=60)
		printf("The grade is E\n");
	else
		printf("The grade is F\n");
	return 0;
}
