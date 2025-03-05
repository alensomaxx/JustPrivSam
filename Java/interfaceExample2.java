//Create a program which will have one interface and 
//more than 2 classes which will implement interface method.

interface Action {
    void performAction();
}

class Jumping implements Action {
    public void performAction() {
        System.out.println("Jumping high!");
    }
}

class Running implements Action {
    public void performAction() {
        System.out.println("Running fast!");
    }
}

class Swimming implements Action {
    public void performAction() {
        System.out.println("Swimming in the water!");
    }
}

public class Main {
    public static void main(String[] args) {
        Action jumper = new Jumping();
        Action runner = new Running();
        Action swimmer = new Swimming();

        jumper.performAction();
        runner.performAction();
        swimmer.performAction();
    }
}