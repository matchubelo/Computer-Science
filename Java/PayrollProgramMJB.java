package Java;
import java.util.Scanner;

public class PayrollProgramMJB 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        PayrollClassesMJB pay = new PayrollClassesMJB();
        PayrollClassesMJB pay2 = new PayrollClassesMJB();


        // EMPLOYEE 1:


        System.out.println("What is your name?");
        pay.setname(scanner.nextLine());

        System.out.println("What is your ID Number?");
        pay.setidnumber(scanner.nextInt());
        scanner.nextLine();

        System.out.println("What is your hourly rate?");
        pay.sethourlyrate(scanner.nextDouble());


        System.out.println("How many hours did you work?");
        pay.sethours(scanner.nextDouble());


        System.out.println("");
        System.out.println("Employee: " + pay.getname());
        System.out.println("Employee ID: " + pay.getidnumber());

        System.out.println(pay.getname() + "'s Gross Pay for " + pay.gethours() + "HRs of work at a rate of $" + pay.gethours() + "/HR is $" + String.format("%.2f", pay.getgrosspay()));

        System.out.println("");
        System.out.println("");
        System.out.println("");




        // EMPLOYEE 2:
        

        System.out.println("What is your name?");
        scanner.nextLine();
        pay2.setname(scanner.nextLine());

        System.out.println("What is your ID Number?");
        pay2.setidnumber(scanner.nextInt());
        scanner.nextLine();

        System.out.println("What is your hourly rate?");
        pay2.sethourlyrate(scanner.nextDouble());


        System.out.println("How many hours did you work?");
        pay2.sethours(scanner.nextDouble());


        System.out.println("");
        System.out.println("Employee: " + pay2.getname());
        System.out.println("Employee ID: " + pay2.getidnumber());
        System.out.println("");
        System.out.println(pay2.getname() + "'s Gross Pay for " + pay2.gethours() + "HRs of work at a rate of $" + pay2.gethours() + "/HR is $" + String.format("%.2f", pay2.getgrosspay()));

        scanner.close();
    }
}
