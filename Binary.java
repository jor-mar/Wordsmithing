import java.util.Stack;

public class Binary {

    public static int toBinary(int n) {
        Stack<Integer> finalStack = new Stack<>();
        String binary = "";
        int nCopy = n;
        while (nCopy > 0) {
            finalStack.push(nCopy % 2);
            nCopy /= 2;
        }
        while (!finalStack.isEmpty()) {
            binary += finalStack.pop();
        }
        return Integer.parseInt(binary);
    }

    public static int fromBinary(int n) {
        int decimal = 0;
        int base = 1;
        while (n > 0) {
            int lastDigit = n % 10;
            n = n / 10;
            decimal += lastDigit * base;
            base = base * 2;
        }
        return decimal;
    }
}