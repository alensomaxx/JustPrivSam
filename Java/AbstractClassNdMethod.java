abstract class Shape {
    public abstract double calculateArea();

    public void displayShapeType() {
        System.out.println("This is a shape.");
    }
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double calculateArea() { // No @Override
        return Math.PI * radius * radius;
    }

    public void displayShapeType() { // No @Override
        System.out.println("This is a circle.");
    }
}

class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double calculateArea() { // No @Override
        return width * height;
    }

    public void displayShapeType() { // No @Override
        System.out.println("This is a rectangle.");
    }
}

class Triangle extends Shape{
    private double base;
    private double height;

    public Triangle(double base, double height){
        this.base = base;
        this.height = height;
    }

    public double calculateArea(){ // No @Override
        return 0.5 * base * height;
    }

    public void displayShapeType() { // No @Override
        System.out.println("This is a triangle.");
    }
}

class ShapeExampleNoOverride {
    public static void main(String[] args) {
        Shape circle = new Circle(5);
        Shape rectangle = new Rectangle(4, 6);
        Shape triangle = new Triangle(3, 8);

        circle.displayShapeType();
        System.out.println("Circle area: " + circle.calculateArea());

        rectangle.displayShapeType();
        System.out.println("Rectangle area: " + rectangle.calculateArea());

        triangle.displayShapeType();
        System.out.println("Triangle area: " + triangle.calculateArea());
    }
}