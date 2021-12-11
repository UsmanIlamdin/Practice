#include<stdio.h>
int main(){
    int first , sec;
    printf("Enter first digit \n");
    scanf("%d",&first);
    printf("Enter Second digit \n");
    scanf("%d",&sec);
    first = first + sec;  // a = a*b;
    sec = first - sec;     // b = a/b;
    first = first -sec;    // a = a*bss

    printf("After swapping number is %d and %d", first, sec);

    return 0;
}

