#include <stdio.h>
#include <math.h>
void main() {
	int num;
	printf("Enter a number : ");
	scanf("%d", &num);
	if(num > 0) {
		if(num == 1)
			printf("%d\n",num);
		else {
			float a = 2.71; 
			long int z =1;
			z=sqrt(2*3.14*num)*pow((num/a),num);
			printf("%ld\n", z);
		}
	} else {
		printf("Invalid input\n");
	}
}
