package Java;
import java.util.*;

public class Payroll7Program 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        Payroll7 payroll = new Payroll7();

        // Input hours and pay rate for each employee
        for (int i = 0; i < 7; i++) {
            int empId = payroll.getEmployeeId(i);

            int hours;
            while (true) {
            System.out.print("Enter hours worked for employee #" + empId + ": ");
            try {
                hours = scanner.nextInt();
                if (hours < 0) {
                System.out.println("Hours must be >= 0.");
                continue;
                }
                break;
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Enter a whole number.");
                scanner.nextLine();
            }
            }
            payroll.setHours(i, hours);

            double payRate;
            while (true) {
            System.out.print("Enter pay rate for employee #" + empId + ": ");
            try {
                payRate = scanner.nextDouble();
                if (payRate < 6.0) {
                System.out.println("Pay rate must be >= 6.0.");
                continue;
                }
                break;
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Enter a number.");
                scanner.nextLine();
            }
            }
            payroll.setPayRate(i, payRate);
        }

        System.out.println("\nEmployee Wages:");
        System.out.println("--------------------------");
        for (int i = 0; i < 7; i++) {
            int empId = payroll.getEmployeeId(i);
            double wage = payroll.getWages(i);
            System.out.printf("Employee #%d: $%.2f\n", empId, wage);
        }
        scanner.close();
    }
}
