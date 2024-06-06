#include <iostream>

using namespace std;

int main() {
  enum directions{North, South, East, West};
  directions home;
  home = East;
  cout<<home<<'\n';
}