//Create an interface named as cook and another interface 
//named driver and create a class which will implement both the 
//interrfaces,the method in cook will be food and that in driver 
//is method drive vehicle.

interface Cook {
    void food();
}

interface Driver {
    void driveVehicle();
}

class MultiSkilledPerson implements Cook, Driver {

    @Override
    public void food() {
        System.out.println("Cooking delicious food.");
    }

    @Override
    public void driveVehicle() {
        System.out.println("Driving the vehicle safely.");
    }
}

public class Main {
    public static void main(String[] args) {
        MultiSkilledPerson person = new MultiSkilledPerson();

        person.food();
        person.driveVehicle();
    }
}