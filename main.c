#include <stdio.h>
#include <stdlib.h>

int main()
{
    int total, number, check;
    total = 0;
    check = 0;
    while(check==0){
        printf("Enter any integer number but, 0. I'll add them up till you put 0.\n");
        scanf("%d", &number);
        if(number !=0){
            check = 0;
            total = number + total;
        }else{
            printf("You entered 0 I will now stop.\nThe total of the numbers you entered is: %d!\n",total);
            check = 1;
        }
    }
    return 0;
}
