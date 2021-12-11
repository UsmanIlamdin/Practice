

#include<stdio.h>
//print factorail of a given number
int main(){
    int num;
    printf("Enter number\n");
    scanf("%d",&num);
    int  fac=1;
    while(num>0){
        fac = fac*num;
        num--;
    }
    printf("factorial of %d is  = %d", num, fac);

    return 0;
}


