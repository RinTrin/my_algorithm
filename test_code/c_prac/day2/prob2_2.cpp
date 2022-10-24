#include <iostream>
#include "minmax.h"

using namespace std;

int main()
{
    MinMax m;
    int a, b, c;
    // int b;
    // int c;
    cout << "a : ";
    cin >> a;
    cout << "b : ";
    cin >> b;
    cout << "c : ";
    cin >> c;
    cout << a << "と" << b << "と" << c << "のうち、最大のものは" << m.max(a, b, c) << endl;
    cout << a << "と" << b << "と" << c << "のうち、最小のものは" << m.min(a, b, c) << endl;
    return 0;
}