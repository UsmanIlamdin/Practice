#include <stdio.h>
#include<string.h>

void reverse(char *a){
    if (*a){
        reverse(a+1);
        printf("%c",*a);
    }
s
}
int main() {
    // Write C code here
    char foo[100];
    printf("Enter string \n");
    gets(foo);

    printf("\n");
    int len = strlen(foo);
    int i = 0;

    // Using loop
    for (i=len-1; i >= 0; i--)
    {
        printf("%c", foo[i]);
    }


    printf("\n \n\ \n ");
    reverse(foo);


    return 0;

}

