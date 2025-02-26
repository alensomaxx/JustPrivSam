class MethodOverloading {

    public int calculate(int a) {
        return a * a; 
    }

    public int calculate(int a, int b) {
        return a * b; 
    }

    public int calculate(int a, int b, int c) {
        return a + b + c; 
    }

    public static void main(String[] args) {
        MethodOverloading obj = new MethodOverloading();

        int result1 = obj.calculate(5);
        int result2 = obj.calculate(5, 10);
        int result3 = obj.calculate(5, 10, 15);

        System.out.println("Result 1 (Square): " + result1);
        System.out.println("Result 2 (Product): " + result2);
        System.out.println("Result 3 (Sum): " + result3);
    }
}