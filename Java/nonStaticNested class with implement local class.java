class Java {

    int test(int a, int b) {
        class sectionk23AL {
            int CalMark() {
                return a * b;
            }
        }
        sectionk23AL sec = new sectionk23AL(); 
        return sec.CalMark(); 
    }

    public static void main(String[] args) {
        Java j = new Java();
        int result = j.test(5, 10);
        System.out.println("Result: " + result); 
    }
}