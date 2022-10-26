#include <iostream>
#include "number.h"

using namespace std;

int main()
{
    Number *pN;
    pN = new Number();
    pN->setNumbers(1, 2);
    cout << pN->getNumbers() << endl;
    delete pN;
    return 0;
}