#include <iostream>
using namespace std;

int main() {
  int a = 3;
  int *p = &a;
  cout<<*p<<'\n';
  a = 4;
  cout<<*p<<'\n';
  *p = 5;
  cout<<*p<<'\n';
  cout<<p<<'\n';
  int &r = a;
  cout<<r<<'\n';
  cout<<&r<<'\n';

  return 0;
}