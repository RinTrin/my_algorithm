#include <iostream>
#include "newcalc.h"

using namespace std;

int main()
{
    NewCalc n;
    int num1;
    int num2;
    cin >> num1;
    cin >> num2;
    n.setNumber1(num1); //  一つ目の数を設定
    n.setNumber2(num2); //  二つ目の数を設定
    cout << n.getNumber1() << " + " << n.getNumber2() << " = " << n.add() << endl;
    cout << n.getNumber1() << " - " << n.getNumber2() << " = " << n.sub() << endl;
    cout << n.getNumber1() << " * " << n.getNumber2() << " = " << n.mul() << endl;
    cout << n.getNumber1() << " / " << n.getNumber2() << " = " << n.div() << endl;

    return 0;
}