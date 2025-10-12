package Java;
import java.util.Scanner;

public class PayrollProgramMJB 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        // EMPLOYEE 1:
        System.out.println("What is your name?");
        String name1 = scanner.nextLine();

        System.out.println("What is your ID Number?");
        int id1 = scanner.nextInt();
        scanner.nextLine(); 

        Payroll pay1 = new Payroll(name1, id1);

        System.out.println("What is your hourly rate?");
        pay1.sethourlyrate(scanner.nextDouble());

        System.out.println("How many hours did you work?");
        pay1.sethours(scanner.nextDouble());
        scanner.nextLine(); 

        System.out.println("");
        System.out.println("Employee: " + pay1.getname());
        System.out.println("Employee ID: " + pay1.getidnumber());
        System.out.println(pay1.getname() + "'s Gross Pay for " + pay1.gethours() + "HRs of work at a rate of $" + pay1.getrate() + "/HR is $" + String.format("%.2f", pay1.getgrosspay()));

        System.out.println("");
        System.out.println("");
        System.out.println("");

        // EMPLOYEE 2:
        System.out.println("What is your name?");
        String name2 = scanner.nextLine();

        System.out.println("What is your ID Number?");
        int id2 = scanner.nextInt();
        scanner.nextLine(); 

        Payroll pay2 = new Payroll(name2, id2);

        System.out.println("What is your hourly rate?");
        pay2.sethourlyrate(scanner.nextDouble());

        System.out.println("How many hours did you work?");
        pay2.sethours(scanner.nextDouble());

        System.out.println("");
        System.out.println("Employee: " + pay2.getname());
        System.out.println("Employee ID: " + pay2.getidnumber());
        System.out.println(pay2.getname() + "'s Gross Pay for " + pay2.gethours() + "HRs of work at a rate of $" + pay2.getrate() + "/HR is $" + String.format("%.2f", pay2.getgrosspay()));

        scanner.close();
    }
}
