class A{
    A(int a){
        System.out.println("Hello Class..."+a);
    }
}

class B extends A{
    B(){
        super(100);
        System.out.println("Hello Section all");
    }
} 

class Demo{
    public static void main(String args[]){
        B r = new B();
        
    }
}