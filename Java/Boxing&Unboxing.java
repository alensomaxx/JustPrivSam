import java.util.Scanner;

class Main{
    public static void main(String args[]){
        Scanner s = new Scanner(System.in);
        int primitiveInt = s.nextInt();
        Integer wrapperInt = primitiveInt;
        
        int prim_int = wrapperInt;
        
        
        System.out.println("Autoboxing: "+wrapperInt);
        
        System.out.println("Unboxing: "+prim_int);
    }
}