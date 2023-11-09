#include <iostream>
#include <math.h>
#define MAX_N 1000
#define PER_LINE 5
using namespace std;

int main() {
  bool notprime[MAX_N + 1];
  int p = 2;
  int counter = 0;
  while (p < MAX_N + 1) {
    if (!notprime[p]) {
      for(int i = 2; i*p < MAX_N + 1; i++) {
        notprime[i*p] = true;
      }
    }
    p++;
  }
  for (int i = 2; i < MAX_N + 1; i++) {
    if (!notprime[i]) {
      cout<<i<<'\t';
      counter++;
    }
    if (counter == PER_LINE) {
      cout<<'\n';
      counter = 0;
    }
  }
  return 0;
}