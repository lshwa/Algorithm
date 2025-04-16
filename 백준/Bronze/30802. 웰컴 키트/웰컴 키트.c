// 웰컴 키트 티셔츠와 펜을 몇장씩 묶어서 줘야하는가?
#include <stdio.h>

int main(void)
{
    unsigned int n;      //  참가자의 수
    int size[6];  //  a 부터 사이즈 S, f는 XXXL 사이즈
    int t, p ;  // t는 티셔츼 묶음 수 , p는 펜의 묶음 수
    int T  = 0;

    scanf("%d", &n);
    scanf("%d %d %d %d %d %d", &size[0], &size[1], &size[2], &size[3], &size[4], &size[5]);
    scanf("%d %d", &t, &p);

    // 티셔츠의 수
    for(int i = 0; i < 6; i++)
    {
        T += size[i] / t;
        T = size[i] % t > 0 ? T + 1 : T;
    }
    printf("%d\n", T);

    // 펜의 수 
    printf("%d %d\n", (n / p), (n % p));

    return 0; 
}