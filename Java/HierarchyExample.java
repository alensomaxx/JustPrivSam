class Vehicle {
    void startEngine() {
        System.out.println("Engine started.");
    }

    void applyBrakes() {
        System.out.println("Brakes applied.");
    }
}

class Car extends Vehicle {
    void openDoors() {
        System.out.println("Car doors opened.");
    }

    void playMusic() {
        System.out.println("Playing music in the car.");
    }
}

class Motorcycle extends Vehicle {
    void wheelie() {
        System.out.println("Performing a wheelie.");
    }

    void lean() {
        System.out.println("Motorcycle leaning into a turn.");
    }
}

class VehicleDemo {
    public static void main(String[] args) {
        Car myCar = new Car();
        Motorcycle myMotorcycle = new Motorcycle();

        myCar.startEngine();
        myCar.openDoors();
        myCar.playMusic();
        myCar.applyBrakes();

        myMotorcycle.startEngine();
        myMotorcycle.wheelie();
        myMotorcycle.lean();
        myMotorcycle.applyBrakes();
    }
}