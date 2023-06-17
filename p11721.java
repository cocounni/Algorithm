import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p11721 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();

        // System.out.println(input);
        for (int i = 0; i < input.length(); ++i) {
            System.out.print(input.charAt(i));
            if (i % 10 == 9) {
            	System.out.println();
            }
        }
    }
}