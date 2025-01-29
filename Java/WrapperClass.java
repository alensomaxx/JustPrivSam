import java.util.Scanner;

class WrapperClassExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Step 1: Take user input as a String
        System.out.print("Enter an integer: ");
        String userInput = scanner.nextLine();

        // Step 2: Convert the String to an Integer (Wrapper Class)
        Integer wrappedInt = Integer.parseInt(userInput);

        // Step 3: Perform operations using the wrapper class
        System.out.println("You entered: " + wrappedInt);
        System.out.println("Binary representation: " + Integer.toBinaryString(wrappedInt));
        System.out.println("Hex representation: " + Integer.toHexString(wrappedInt));
        System.out.println("Is the number even? " + (wrappedInt % 2 == 0));

        // Step 4: Autoboxing and Unboxing
        int primitiveInt = wrappedInt; // Unboxing: Converting Integer to int
        Integer anotherWrappedInt = primitiveInt; // Autoboxing: Converting int to Integer

        System.out.println("Primitive int: " + primitiveInt);
        System.out.println("Another Wrapped Integer: " + anotherWrappedInt);

        scanner.close();
    }
}