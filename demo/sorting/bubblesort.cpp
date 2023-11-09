#include <iostream>

using namespace std;

void swap(int &a, int &b) {
    int c = a;
    a = b;
    b = c;
}

void bubbleSort(int data[], int n) {
    for (int i = n - 2; i >= 0; i--) { 
    // i 是当前这一轮检查的最后一对相邻元素中左边一个的编号，每一轮过后，下一轮短一点
        for (int j = 0; j <= i; j++) {
            // j 是当前检查的这一对中左边一个的编号
            if (data[j] > data[j+1]) { // 如果顺序不对
                swap(data[j], data[j+1]);
            }
        }
    }
}

int main() {
    int data[] = {3, 8, 2, 6, 1, 9, 4, 2, 5};
    bubbleSort(data, sizeof(data) / sizeof(data[0]));
    for (int num: data) cout<<num<<" ";

    return 0;
}