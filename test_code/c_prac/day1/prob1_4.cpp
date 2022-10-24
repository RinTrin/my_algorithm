#include <iostream>
#include <string>

using namespace std;

int main()
{
    string num;
    cout << "数字を入力してください："; //+  << endl;
    cin >> num;
    cout << num + "を2倍した数は、" + to_string(stoi(num) * 2) + "です" << endl;
    return 0;
}