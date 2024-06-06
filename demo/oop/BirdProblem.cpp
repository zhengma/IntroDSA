/**
 * APCSA 经典疑难考题 “Bird Problem” 的 C++ 转译
 * 用于展示 C++ 与 Java 的细节差异
 * 
 * 作者: 马正
 * 组织: 渊学通教育广州分校
 * 创建日期: Jun. 3, 2024
 * 最后修改日期: Jun. 3, 2024
 * 编译器版本: g++ 13.2.0
 */

#include <iostream>
using namespace std;

class Bird {
  public:
    virtual void act() const {
      cout<<"fly ";
      makeNoise();
    }

    // 尝试仅仅去掉下面这行的 "virtual"，解释运行结果
    // 从这个角度看，Java 中所有可重写（非静态、非final、
    // 非私有）方法全都天生是虚方法
    virtual void makeNoise() const {
      cout<<"chirp ";
    }
};

class Dove : public Bird {
  public:
    void act() const override {
      Bird::act();
      cout<<"waddle ";
    }

    void makeNoise() const {
      Bird::makeNoise();
      cout<<"coo ";
    }
};

int main() {
  Bird* pigeon = new Dove();
  pigeon->act();
  return 0;
}