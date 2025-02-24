class Animal {
    void sound(){
        System.out.println("This is an animal");
    }
}

class Dog extends Animal {
    void bark(){
        System.out.println("BOW! BOW! BOW!");
    }
}

public class Main{
    public static void main(String[] args){
        Dog mydog = new Dog();
        mydog.sound();
        mydog.bark();
    }
}