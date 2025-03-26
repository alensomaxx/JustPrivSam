import java.util.*;
import java.util.function.Predicate;

class CombinedExamples {

    public static void main(String[] args) {
        // Inbuilt Predicate Example
        List<Integer> numbers = Arrays.asList(10, 15, 20, 25, 30);
        Predicate<Integer> isEven = num -> num % 2 == 0;
        Predicate<Integer> isGreaterThan15 = num -> num > 15;

        System.out.println("Predicate: Even Numbers: ");
        numbers.stream().filter(isEven).forEach(System.out::println);

        System.out.println("Predicate: Numbers > 15: ");
        numbers.stream().filter(isGreaterThan15).forEach(System.out::println);

        // Runnable Example
        new Thread(() -> {
            for (int i = 0; i < 3; i++) {
                System.out.println("Runnable: " + i);
            }
        }).start();

        // Comparator Example
        List<Integer> nums = Arrays.asList(5, 2, 8, 1, 3);
        nums.sort((a, b) -> a - b);
        System.out.println("Comparator: Sorted Ascending: " + nums);

        nums.sort((a, b) -> b - a);
        System.out.println("Comparator: Sorted Descending: " + nums);
    }
}