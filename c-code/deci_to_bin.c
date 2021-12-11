
#include<stdio.h>
int main(){
    int deci;
    printf("Enter decimal number \n");
    scanf("%d",&deci);
    int rem,bin , i=1 , sum=0;
    while(deci!=0){
        rem =deci%2;
        sum +=rem*i;
        deci /=2;
        i*=10;
    }
    printf("Binary number is %d",sum);

    return 0;
}

