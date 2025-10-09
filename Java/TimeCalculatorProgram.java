package Java;
import java.util.Scanner;

public class TimeCalculatorProgram 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number of seconds: ");
        int seconds = scanner.nextInt();

        if (seconds >= 86400) {
            double days = seconds / 86400.0;
            System.out.printf("That is %.2f days.%n", days);
        } else if (seconds >= 3600) {
            double hours = seconds / 3600.0;
            System.out.printf("That is %.2f hours.%n", hours);
        } else if (seconds >= 60) {
            double minutes = seconds / 60.0;
            System.out.printf("That is %.2f minutes.%n", minutes);
        } else {
            System.out.println(seconds + " Seconds");
        }

        scanner.close();
    }
}
