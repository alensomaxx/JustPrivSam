import java.util.Scanner;
class main{
    public static void main(String[]args){
        Scanner obj = new Scanner (System.in);
        int N = obj.nextInt();
        int on = N;
        int evenCount = 0;
        
        while(N>0){
            int digit = N%10;
            if (digit %2 == 0){
                evenCount++;
            }
            N=N/10;
        }
        if (evenCount == 0){
            System.out.println("There are no even digit in the number");
        }else if (on % evenCount == 0 ){
            System.out.println("It is a divisor of the orginal number");
        }else{
            System.out.println("It is not a divisor of the orginal number");
        }
    }
}