import java.util.*;

class ComparatorExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(5, 2, 8, 1, 3);

        Collections.sort(numbers, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                return a - b;
            }
        });
        System.out.println("Sorted in Ascending Order: " + numbers);

        numbers.sort((a, b) -> b - a);
        System.out.println("Sorted in Descending Order: " + numbers);
    }
}