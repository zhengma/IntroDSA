#include <iostream>
#include <set>

using namespace std;

int main() {
  set<char> set_of_chars;
  string str = "Hello World!";
  for (char c: str) {
    set_of_chars.insert(c);
  }
    
  for (char c: set_of_chars) {
    cout<<c<<' ';
  }
  return 0;
}