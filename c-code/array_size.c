#include <stdio.h>
int main()
{
    int ArraySize = 0 ;
    int  arr[] = {10, 20, 30, 40, 50, 60};
    //Calculate array size using pointer arithmetic
    ArraySize = *(&arr + 1) - arr;
    printf("arr is = %d \n ",arr);
    printf("pointer  is = %d \n " ,*(&arr + 1) );

    printf("Array size = %d",ArraySize);
    return 0;
}
