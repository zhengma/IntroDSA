#include <iostream>
#include <math.h>
#define TIMES 2
#define OUTPUT(m, n) (cout<<m<<'\t'<<n<<'\t'<<m-n<<'\n')

using namespace std;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void reduce(int *m, int *n, int by) {
    cout<<"Take "<<by<<" from both:\n";
    *m -= by;
    *n -= by;
    OUTPUT(*m, *n);
}

void multiply(int *m, int *n) {
    cout<<"Multiply n by "<<TIMES<<":\n";
    *n *= TIMES;
    OUTPUT(*m, *n);
}

void takeall(int m, int n) {
    int reduceto;
    
    if (m < n) swap(&m, &n);
    OUTPUT(m, n);
    while (m > n * TIMES) {
        multiply(&m, &n);
    }
    while (m != n) {
        reduceto = ceil(((double)m - n)/TIMES);
        reduce(&m, &n, n-reduceto);
        multiply(&m, &n);
    }
    reduce(&m, &n, n);
}

int main() {
    takeall(654, 123);
    return 0;
}