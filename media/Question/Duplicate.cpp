#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> array;
    int n, a;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        array.push_back(a); /* code */
    }
    for (int i = 0; i < n; i++)
    {
        if (array[abs(array[i])] >= 0)
        {
            // cout << array[abs(array[i])] << " " << abs(array[i]) << endl;
            array[abs(array[i])] = -array[abs(array[i])];
        }
        else
        {
            cout << abs(array[i]) << endl;
        } /* code */
    }

    return 0;
}