#include<stdio.h>
int lg(int n1,int n2);
int main(){
	int n1,n2;
	printf("Enter two numbers : ");
	scanf("%d%d",&n1,&n2);
	lg(n1,n2);
}
int lg(int n1,int n2){
	int g,l,rem,num,den;
	if(n1>n2){
		num=n1;
		den=n2;
	}
	else{
		num=n2;
		den=n1;
	}
	rem=num%den;
	while(rem!=0){
		num=den;
		den=rem;
		rem=num%den;
	}
	g=den;
	l=(n1*n2)/g;
	printf("LCM of %d and %d is %d\n",n1,n2,l);
	printf("GCD of %d and %d is %d\n",n1,n2,g);
	return 0;
}
