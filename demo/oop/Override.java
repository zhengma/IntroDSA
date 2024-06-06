/**
 * 
 */

class Student {
    private String name;
    private String id;
    private double gpa;
    
    public void bonusGPA() {
        this.gpa += 0.5;
    }
    
    public Student(String name, String id, double gpa) {
        this.name = name;
        this.id = id;
        this.gpa = gpa;
    }
    
    public String toString() {
        return "Name: " + this.name + "\nStudent ID: " + this.id;
    }
    
    public double getGpa() {
        return this.gpa;
    }
    
    public void setGpa(double newGpa) {
        this.gpa = newGpa;
    }
}

class UndergradStudent extends Student {
    private String major;
    
    UndergradStudent(String name, String id, double gpa, String major) {
        super(name, id, gpa);
    }
    
    public String getMajor() {
        return this.major;
    }
}

class GradStudent extends Student {
    private String interest;
    
    public void bonusGPA() {
        super.bonusGPA();
        setGpa(getGpa() + 0.25);
    }
    
    public void penalty() {
        double oldGpa = getGpa();
        double newGpa = oldGpa - 0.5;
        setGpa(newGpa);
    }
    
    GradStudent(String name, String id, double gpa, String interest) {
        super(name, id, gpa);
        this.interest = interest;
    }
    
    public String getInterest() {
        return this.interest;
    }
}

public class Override {
	public static void main(String[] args) {
		Student oneStudent = new Student("David", "123456", 3.8);
		System.out.println(oneStudent);
		System.out.println("Before bonus: " +  oneStudent.getGpa());
		oneStudent.bonusGPA();
		System.out.println("After bonus: " + oneStudent.getGpa());
    	Student oneUG = new UndergradStudent("Pony", "654321", 3.2, "Physics");
		System.out.println(oneUG);
		System.out.println("Before bonus: " +  oneUG.getGpa());
		oneUG.bonusGPA();
		System.out.println("After bonus: " + oneUG.getGpa());
		Student oneGrad = new GradStudent("Zheng", "5322001", 4.0, "Physics");
		System.out.println(oneGrad);
		System.out.println("Before bonus: " +  oneGrad.getGpa());
		oneGrad.bonusGPA();
		System.out.println("After bonus: " + oneGrad.getGpa());
		GradStudent surelyGrad = (GradStudent)oneGrad;
		surelyGrad.penalty();
		System.out.println("After penalty: " + oneGrad.getGpa());
	}
}