#include "data.h"
#include <string>

void CData::init()
{
    number = 0;
    comment = "";
}
void CData::setNumber(int snum)
{
    number = snum;
}
void CData::setComment(string scom)
{
    comment = scom;
}
int CData::getNumber()
{
    return number;
}
string CData::getComment()
{
    return comment;
}