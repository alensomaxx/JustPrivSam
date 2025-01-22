import java.util.Scanner;
class Logical{
   
    public static void main(String[] args){
        Scanner myobj = new Scanner(System.in);
        int a = myobj.nextInt();
        int b = myobj.nextInt();
        System.out.println((a+b>a-b)&&(a*b<a/b));
        System.out.println((a*b>a/b)||(a/b<a%b));
        System.out.println(!((a*b>a/b)||(a/b<a%b)));
       
       
       
    }
   
}
