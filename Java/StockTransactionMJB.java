package Java;

public class StockTransactionMJB 
{
    public static void main(String[] args) 
    {
       // Background Info
        Integer shares = 1000;
        Double commisionrate = 0.02;
        
        // Purchase Details
        Double buyshareprice = 32.87;

        // Sell Details
        Double sellshareprice = 33.92;

        // Calculations
        Double totalstockbuyprice = (shares * buyshareprice);
        Double brokerbuycommission = (totalstockbuyprice * commisionrate);
        Double totalstocksellprice = (shares * sellshareprice);
        Double brokersellcommission = (totalstocksellprice * commisionrate);
        Double profit = (totalstocksellprice - totalstockbuyprice - brokerbuycommission - brokersellcommission);

        // Print Statements
        System.out.println("Joe paid $" + String.format("%.2f", totalstockbuyprice) + " for " + shares + " shares of stock");
        System.out.println("Joe paid his broker $" + String.format("%.2f", brokerbuycommission) + " when buying the stock");
        System.out.println("Joe gained $" + String.format("%.2f", totalstocksellprice) + " for selling " + shares + " shares of stock");
        System.out.println("Joe paid his broker $" + String.format("%.2f", brokersellcommission) + " when selling the stock");

        if (profit < 0) {System.out.println("Since Joe's profit was negative, he lost $" + String.format("%.2f", (profit * -1)));} 
        else {System.out.println("Joes total profit was: $" + String.format("%.2f", profit));}
    }
}
