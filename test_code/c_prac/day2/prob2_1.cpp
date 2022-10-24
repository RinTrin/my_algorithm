#include <iostream>
#include "keisan.h"

using namespace std;

int main()
{
    Keisan k;
    k.a = 10;
    k.b = 3;
    cout << k.a << " + " << k.b << " = " << k.add() << endl;
    cout << k.a << " - " << k.b << " = " << k.sub() << endl;
    return 0;
}