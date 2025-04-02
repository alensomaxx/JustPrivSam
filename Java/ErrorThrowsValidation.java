import java.util.Scanner;

class ExceptionHandlingExample {
    public static void validateNumber(int num) throws IllegalArgumentException {
        if (num < 0) {
            throw new IllegalArgumentException("Negative numbers are not allowed");
        }
        if (num > 10) {
            throw new IllegalArgumentException("Number too large! Must be 10 or less.");
        }
        System.out.println("Valid Number Entered: " + num);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            int num = scanner.nextInt();

            validateNumber(num);

            System.out.println("Enter a divisor: ");
            int divisor = scanner.nextInt();
            int result = 100 / divisor;

            System.out.println("100 divided by your number is: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Error: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            System.out.println("IllegalArgumentException: " + e.getMessage());
        } finally {
            System.out.println("Finally block Executed. Cleanup done!");
            scanner.close();
        }
    }
}