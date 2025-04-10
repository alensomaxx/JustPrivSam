import java.util.*;

class Main{
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNextInt()){
            int num = scanner.nextInt();
            System.out.println("The Number is: "+num);
        }else{
            System.err.println("Error");
        }
        scanner.close();
    }
}