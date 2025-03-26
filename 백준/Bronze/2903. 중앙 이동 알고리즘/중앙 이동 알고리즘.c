// 중앙 이동 알고리즘 
// 처음은 3의 제곱 , 5의 제곱, 9의 제곱 등으로 커져나감.. 수열을 찾아내어 계산
#include <stdio.h>

int main(void)
{
    int n, dot = 3, inc = 2;
    scanf("%d", &n);

    for(int i = 1; i < n; i++)
    {
        dot += inc;
        inc *= 2;
    }

    printf("%d\n", dot * dot);

    return 0;
}