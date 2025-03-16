#include <stdio.h>
void fibonacci(int n);

int main(void){
    int t,n;
    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        scanf("%d", &n);
        fibonacci(n);
    }
    
}

void fibonacci(int n)
{
    int last, current, result;
    current = 1, last = result = 0;
    int i;
    for(int i = 0; i <= n ; i++){
        last = current;
        current = result;
        result = last + current;
    }
    printf("%d %d\n", last, current);
}