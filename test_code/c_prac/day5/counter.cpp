#include "counter.h"
#include <iostream>

using namespace std;

int Counter::m_totalCount = 0;

//  コンストラクタ（カウント回数を0で初期化）
Counter::Counter() : m_count(0)
{
}
void Counter::reset()
{
    m_totalCount -= m_count;
    m_count = 0;
    cout << "reset:" << to_string(m_totalCount) << endl;
}
void Counter::count()
{
    m_count++;
    m_totalCount++;
    cout << "count:" << m_totalCount << endl;
}
int Counter::getCount()
{
    return m_count;
}
int Counter::getTotalCount()
{
    return m_totalCount;
}