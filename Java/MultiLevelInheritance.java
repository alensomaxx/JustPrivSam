class A {
    void add(int a, int b) { System.out.println(a + b); }
    void sub(int a, int b) { System.out.println(a - b); }
}

class B extends A {
    void multiplication(int a, int b) { System.out.println(a * b); }
    void division(int a, int b) { System.out.println(a / b); }
}

class C extends B {
    void remainder(int a, int b) { System.out.println(a % b); }
}

class MultiLevel {
    public static void main(String[] args) {
        C c = new C();
        c.add(10, 5);
        c.multiplication(10, 5);
        c.remainder(10, 3);
    }
}