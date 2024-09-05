/**
 * 回答学生提问: "在一个没有乘除法指令的指令集 (比如'CAIE指令集')上,
 * 能否只用加减和其它位运算达到乘除法的效果?"
 * 
 * 也适宜于让学生自己分析以下代码为何能奏效.
 * 
 * 作者: 马正
 * 组织: 渊学通教育广州分校
 * 创建日期: Sep. 5, 2024
 * 最后修改日期: Sep. 5, 2024
 * 编译器版本: g++ 13.2.0
 */
#include <iostream>

using namespace std;

int MulUnsigned(int a, unsigned b) {
  int product = 0;
  while (b > 0) {
    if ((b & 1) != 0) {
      product += a;
    }
    b >>= 1;
    a <<= 1;
  }
  return product;
}

int Mul(int a, int b) {
  if (b >= 0) {
    return MulUnsigned(a, b);
  }
  return ~MulUnsigned(a, ~b + 1) + 1;
}

int DivUnsigned(int a, int b, int& remainder) {
  int quotient = 0;
  int backup = b;
  while (b <= a) {
    b <<= 1;
  }
  while (b != backup) {
    b >>= 1;
    quotient <<= 1;
    if (b <= a) {
      a -= b;
      quotient++;
    }
  }
  remainder = a;
  return quotient;
}

int Div(int a, int b, int& r) {
  int q = DivUnsigned((a >= 0) ? a : ~a + 1, (b > 0) ? b : ~b + 1, r);
  r = (a >= 0) ? r : (~r + 1);
  return ((a ^ b) > 0) ? q : (~q + 1);
}

int DivPython(int a, int b, int& r) {
  int q = Div(a, b, r);
  return q + Div(r + b, b, r) - 1;
}

int main() {
  cout<<"155 x (-11) = "<<Mul(155, -11)<<'\n';
  int r;
  cout<<"155 / 11 = "<<DivUnsigned(155, 11, r)<<' '<<r<<'\n';
  cout<<"156 / (-11) = "<<Div(156, -11, r)<<' '<<r<<'\n';
  cout<<"156 / (-11) = "<<DivPython(156, -11, r)<<' '<<r<<" in Python.\n";
  return 0;
}