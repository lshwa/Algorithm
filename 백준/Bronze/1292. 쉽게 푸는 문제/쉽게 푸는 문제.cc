#include <iostream>
using namespace std;

int main(void)
{
    int a, b;
    int count = 0; int sum = 0;
    int arr[1000];

    cin >> a >> b;
    for(int i = 1; i <= 1000; i++)
    {
        for(int j = 0; j < i && count < 1000; j++)
            arr[count++] = i;
    }
    for(int i = a - 1; i < b; i++)
    {
        sum += arr[i];
    }
    cout << sum;
    return 0;

}