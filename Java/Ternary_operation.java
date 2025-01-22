import java.util.Scanner;

class main{
    public static void main(String args[]){
        
        Scanner myobj = new Scanner (System.in);
        
        int a = myobj.nextInt();
        int b = myobj.nextInt();
        
        int min = (a < b)? a:b;
        
        System.out.println("By comparing "+a+" and "+b);
        System.out.println(("Minimum Value : "+min));
        
    }
}