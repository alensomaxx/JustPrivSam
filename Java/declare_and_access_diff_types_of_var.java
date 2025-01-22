class Main {
    int a = 10; // Instance variable

    

    static int c = 40; // Static variable

    public static void main(String[] args) {
        int b = 30; // Local variable
        final int D = 20; // Constant
        Main t = new Main(); 

        System.out.println(t.a); // Access instance variable through object
        System.out.println(b); 
        System.out.println(c); // Access static variable directly
        System.out.println(D); // Access constant directly
    }
}