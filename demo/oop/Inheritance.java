package demo.oop;

/**
 * 原本为AP Computer Science A Unit 9: Inheritance 设计
 * 展示的主要考点：
 * 1. 类的继承
 * 2. 构造器的重载
 * 3. 子类的构造器
 * 4. Object.toString() 的重载
 */

class Student {
    private String name;
    private String id;
    private int[] scores;
    private double gpa;
    
    public Student(String name, String id) {
        this.name = name;
        this.id = id;
    }
    
    public Student(String name) {
        this.name = name;
        this.id = "12345678";
    }
    
    public Student() {
        this.name = "unknown";
        this.id = "87654321";
    }
    
    public String toString() {
        return "Name: " + this.name + "\nStudent ID: " + this.id;
    }
}

class Undergrad extends Student {
    private boolean isHonor;
    
    public Undergrad(String name, String stuNo, boolean isHonor) {
        super(name, stuNo);
        this.isHonor = isHonor;
    }
}

public class Inheritance
{
	public static void main(String[] args) {
	    Student pony = new Student("Zheng", "05322001");
		System.out.println(pony);
		Student jessica = new Student("Jessica");
		System.out.println(jessica);
		Student johndoe = new Student();
		System.out.println(johndoe);
	}
}