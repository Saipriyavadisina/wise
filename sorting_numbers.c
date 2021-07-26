#include<stdio.h>
 int main()
{
    int Size, i, a[10];
    printf("Enter the Size of an Array : ");
    scanf("%d", &Size);
    int Even_Count = 0, Odd_Count = 0;
    printf("Enter the Array Elements : ");
    for(i = 0; i < Size; i++)
    {
        scanf("%d", &a[i]);
    }
    for(i = 0; i < Size; i ++)
    {
        if(a[i] % 2 == 0)
        {
            Even_Count++;
        }
        else
        {
            Odd_Count++;
        }
    }
    printf("Number of Even Numbers in Array = %d ",
    Even_Count);
    printf("\nNumber of Odd Numbers in Array = %d ",
    Odd_Count);
    return 0;
}
