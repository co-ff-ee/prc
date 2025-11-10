import java.util.Scanner;

public class B1 
{
    static {
        System.loadLibrary("B1");
    }

    public native int add(int num1, int num2);
    public native int sub(int num1, int num2);
    public native int mult(int num1, int num2);
    public native double div(int num1, int num2);

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num1, num2;
        System.out.println("DLL Example Operations");
        System.out.print("Enter first number: ");
        num1 = scanner.nextInt();
        System.out.print("Enter second number: ");
        num2 = scanner.nextInt();

        B1 obj = new B1();
        System.out.println("Addition Result: " + obj.add(num1, num2));
        System.out.println("Subtraction Result: " + obj.sub(num1, num2));
        System.out.println("Multiplication Result: " + obj.mult(num1, num2));
        System.out.println("Division Result: " + obj.div(num1, num2));
    }
}



