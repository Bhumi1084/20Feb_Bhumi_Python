#include<stdio.h>
int main(){
	int n;
	printf("Enter number : ");
	scanf("%d",&n);
	if(n==0 || n==1){
		printf("number is not prime");
	}
	else if(n%2==0){
		printf("number is prime");
	}
	else{
		printf("number is not prime");
	}
	return 0;
}
