/**
 * 记录除法运算的商和余数.
 * 
 * <p>Java 同时返回超过一个值是非常非常麻烦的.
 */
class DivisionResult {

  private int quotient;
  private int remainder;
  
  public DivisionResult(int q, int r) {
    this.quotient = q;
    this.remainder = r;
  }

  public int getQuotient() {
    return this.quotient;
  }

  public int getRemainder() {
    return this.remainder;
  }

  public String toString() {
    return "(" + this.quotient + ", " + this.remainder + ")";
  }
}

/**
 * 回答学生提问: "在一个没有乘除法指令的指令集 (比如'CAIE指令集')上,
 * 能否只用加减和其它位运算达到乘除法的效果?"
 * 
 * <p>也适宜于让学生自己分析以下代码为何能奏效.

 * @author 马正
 * @version 1.0
 * @since Sep. 1, 2024
 */
public class MulDiv {

  /**
   * 模拟在精简指令集上计算两个整数 (其中之一应为非负整数) 的积.
   * 
   * <p>运算指令只用到 ADD, AND, LSL 和 LSR.

   * @param a 被乘数, 任意整数.
   * @param b 乘数, 须为非负整数.
   * @return a * b 的结果.
   */
  private static int mulUnsigned(int a, int b) {
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

  /**
   * 模拟在精简指令集上计算两个整数的积.
   * 
   * <p>运算指令只用到 ADD, AND, INC, LSL, LSR 和 NOT.

   * @return a * b 的积.
   */
  public static int mul(int a, int b) {
    if (b >= 0) {
      return mulUnsigned(a, b);
    }
    return ~mulUnsigned(a, ~b + 1) + 1;
  }

  /**
   * 模拟在精简指令集上计算两个非负整数的商和余数.
   * 
   * <p>运算指令只用到 SUB, INC, LSL 和 LSR.

   * @param a 被除数, 须为非负整数.
   * @param b 除数, 须为正整数.
   * @return 将 {@code a / b} 和 {@code a % b} 打包为一个 {@code DivisionResult} 对象.
   */
  private static DivisionResult divUnsigned(int a, int b) {
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
    return new DivisionResult(quotient, a);
  }

  /**
   * 模拟在精简指令集上计算两个整数的商和余数.
   * 
   * <p>运算指令只用到 SUB, INC, LSL, LSR, NOT 和 XOR.

   * @param a 被除数, 任意整数.
   * @param b 除数, 任意非零整数.
   * @return 将 {@code a / b} 和 {@code a % b} 打包为一个 {@code DivisionResult} 对象.
   */
  public static DivisionResult div(int a, int b) {
    DivisionResult result = divUnsigned((a >= 0) ? a : ~a + 1, (b > 0) ? b : ~b + 1);
    int quotient = result.getQuotient();
    int remainder = result.getRemainder();
    if ((a ^ b) < 0) {
      quotient = ~quotient + 1;
    }
    if (a < 0) {
      remainder = ~remainder + 1;
    }
    return new DivisionResult(quotient, remainder);
  }

  /**
   * 计算两个整数按 Python 规则的商和余数.
   * 
   * <p>在Python中, 若 b < 0, 则 {@code b < (a % b) <= 0}.
   * 无论如何, 仍总有 {@code a == b * (a // b) + (a % b)}.

   * @param a 被除数, 任意整数.
   * @param b 除数, 任意非零整数.
   * @return 将Python中计算 {@code a // b} 和 {@code a % b} 的结果
   *      打包为一个 {@code DivisionResult} 对象.
   */
  public static DivisionResult divPython(int a, int b) {
    DivisionResult result = div(a, b);
    DivisionResult offset = div(result.getRemainder() + b, b);
    return new DivisionResult(result.getQuotient() + offset.getQuotient() - 1,
        offset.getRemainder());
  }

  /**
   * 测试方法.
   */
  public static void main() {
    System.out.println(MulDiv.mul(155, -11));
    System.out.println(MulDiv.div(155, -11));
    System.out.println(MulDiv.divPython(155, -11));
    // System.out.println(test.div());
    // System.out.println(test.mod());
  }
}
