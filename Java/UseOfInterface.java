import java.util.Scanner;

interface client {
    void input();
    void output();
}

class R implements client {
    String name;
    double sal;

    public void input() {
        Scanner obj = new Scanner(System.in);
        System.out.println("Enter Name: ");
        name = obj.nextLine(); // Corrected: Assign input to class member 'name'
        System.out.println("Enter salary: ");
        sal = obj.nextDouble(); // Corrected: Assign input to class member 'sal'
    }

    public void output() {
        System.out.println("Name: " + name);
        System.out.println("Salary: " + sal);
    }

    public static void main(String[] args) {
        R Client = new R(); // Corrected: Use class R instead of 'details'
        Client.input();
        Client.output();
    }
}