#include <iostream>
using namespace std;

int main(void)
{
    int n;
    cin >> n;
    long long arr[91];

    arr[0] = 0;
    arr[1] = 1;
    for(int i = 2; i <= n; i++)
    {
        arr[i] = arr[i-1] + arr[i-2];
    }
    cout << arr[n] << '\n';
    return 0;
}