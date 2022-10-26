#include "number.h"
#include <iostream>

using namespace std;

//  二つの数値を設定
Number::Number() : a(2), b(4)
{
    cout << "st" << endl;
}
void Number::setNumbers(int n1, int n2)
{
    cout << a << " " << b << endl;
    a = n1;
    b = n2;
}
int Number::getNumbers()
{
    return a + b;
}
Number::~Number()
{
    cout << "fi" << endl;
}