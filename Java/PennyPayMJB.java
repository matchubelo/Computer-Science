package Java;
import java.util.*;

public class PennyPayMJB 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter number of days (>=1): ");
        int days = 0;
        while (days < 1) {
            if (scanner.hasNextInt()) {
                days = scanner.nextInt();
                if (days < 1) {
                    System.out.print("Please enter a positive integer: ");
                }
            } else {
                scanner.next();
                System.out.print("Invalid input. Enter a positive integer: ");
            }
        }

        int payInPennies = 1; // start with 1 cent
        int totalPennies = 0;

        System.out.println("\nDay\tPay");
        for (int count = 1; count <= days; count++) 
        {
            
            double dollars = payInPennies / 100.0;

            System.out.printf("%d\t$%.2f%n", count, dollars);
            totalPennies += payInPennies;
            payInPennies *= 2;
        }

        System.out.printf("%nTotal pay: $%.2f%n", totalPennies / 100.0);
        scanner.close();
    }
}
