#include <stdio.h>
int main()
{
    int a[1000],i,n,even=0,odd=0;
    printf("Enter size of the array : ");
    scanf("%d",&n);
    printf("Enter elements : ");
    for(i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }
     for(i=0; i<n; i++)
    {
          if(a[i] % 2 == 0)
          even++;
          else
          odd++;
    }
     printf("even numbers in array: %d\n",even);
     printf("odd numbers in array: %d",odd);
    return 0;
}
