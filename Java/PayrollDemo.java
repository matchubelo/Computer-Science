package Java;

public class PayrollDemo 
{

    public static void main(String[] args) 
    {
        PayrollClassesMJB pay = new PayrollClassesMJB();
        pay.setname("Matt Belo");
        pay.sethours(15);
        pay.sethourlyrate(16.89);

        System.out.println("This is your gross pay: $" + String.format("%.2f", pay.getgrosspay()));
        
    }
    
}
