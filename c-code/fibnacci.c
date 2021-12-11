

#include<stdio.h>
//print fibonacci of first
int main(){
    int num;
    printf("Enter number upto which fibonacci want to print\n");
    scanf("%d",&num);
    int  i, first=0 , second =1 , result=0;
    for (i=0 ; i<=num ; i++){
            if(i<=0)
            {
                result =i;
            }
            else
            {
                    result= first + second;
                    first = second;
                    second = result;
            }
            printf("%d \n", result);
    }
    return 0;
}

