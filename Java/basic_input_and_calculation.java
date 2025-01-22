import java.util.Scanner;

class main{
    public static void main(String args[]){
        
        Scanner myobj = new Scanner (System.in);
        
        int a = myobj.nextInt();
        int b = myobj.nextInt();
        
        System.out.println("Addition: "+(a+b));
        System.out.println("Difference: "+(a-b));
        System.out.println("Product: "+(a*b));
        System.out.println("Quotient: "+(a/b));
        System.out.println("Remainder: "+(a%b));
    }
}