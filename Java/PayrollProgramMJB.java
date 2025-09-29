package Java;
import java.util.Scanner;

public class PayrollProgramMJB 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        PayrollClassesMJB pay = new PayrollClassesMJB();

        System.out.println("What is your name?");
        pay.setname(scanner.nextLine());

        System.out.println("What is your ID Number?");
        pay.setidnumber(scanner.nextInt());
        
        System.out.println("What is your hourly rate?");
        pay.sethourlyrate(scanner.nextDouble());

        System.out.println("How many hours did you work?");
        pay.sethours(scanner.nextDouble());

        System.out.println("");
        System.out.println("Employee: " + pay.getname());
        System.out.println("Employee ID: " + pay.getidnumber());
        System.out.println("");
        System.out.println(pay.getname() + "'s Gross Pay for " + pay.gethours() + "HRs of work at a rate of $" + pay.gethours() + "/HR is $" + String.format("%.2f", pay.getgrosspay()));


        scanner.close();
    }
}
