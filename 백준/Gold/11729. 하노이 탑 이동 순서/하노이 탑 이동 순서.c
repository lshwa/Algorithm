// 하노이탑 문제 
#include <stdio.h>
#include <math.h>

void HanoiTowerMove(int num, int from, int by, int to)
{
    if(num == 1)
    {
        printf("%d %d\n", from, to);
    }
    
    else
    {
        HanoiTowerMove(num - 1, from , to , by);
        printf("%d %d\n", from ,to);
        HanoiTowerMove(num -1, by, from, to);
    }
}

int main(void)
{
    int k;
    int count;
    scanf("%d", &k);
    count = pow(2, k) - 1;
    printf("%d\n", count);
    HanoiTowerMove(k, 1, 2, 3);

    return 0; 
}