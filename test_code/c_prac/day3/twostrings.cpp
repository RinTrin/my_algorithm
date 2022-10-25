#include <iostream>
#include "twostrings.h"
#include <string>

//  一つ目の文字列を設定
void TwoStrings::setString1(string s)
{
    m_string1 = s;
}
//  二つ目の文字列を設定
void TwoStrings::setString2(string s)
{
    m_string2 = s;
}
//  一つ目の文字列を取得
string TwoStrings::getString1()
{
    return m_string1;
}
//  二つ目の文字列を取得
string TwoStrings::getString2()
{
    return m_string2;
}
//  二つの文字列をつないだものを取得
string TwoStrings::getConnectedString()
{
    ap_str.append(m_string1);
    ap_str.append(m_string2);
    return ap_str;
}
//  getConnectedString()で得られる文字列の長さを取得
int TwoStrings::getConnectedLength()
{
    return ap_str.length();
}