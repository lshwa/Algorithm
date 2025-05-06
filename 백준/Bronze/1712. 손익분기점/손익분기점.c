// 손익분기점 문제 C 언어
#include <stdio.h>

int main()
{
    int A, B, C;
    int point;
    scanf("%d %d %d", &A, &B, &C);
    
    if (B >= C)
        printf("-1\n");
    else
        printf("%d\n", A / (C - B) + 1);

    return 0;
}