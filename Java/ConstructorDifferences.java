public class Main{
    int id;
    String name;
    
    public Main(){
        System.out.println("This is a default constructor");
    }
    
    public Main(int i, String n){
        id = i;
        name = n;
    }
    
    public static void main(String[] args){
        Main s = new Main();
        System.out.println("\nDefault Constructor values: \n");
        System.out.println("Student Id: "+s.id + "\nStudent Name: "+s.name);
        
        
        System.out.println("\nParameterized Constructor values: \n");
        Main student = new Main(10, "David");
        
        System.out.println("Student ID: "+student.id + "\nStudent Name: "+student.name);
    }
}