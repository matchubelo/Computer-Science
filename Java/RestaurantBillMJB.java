package Java;

import java.util.Scanner;

public class RestaurantBillMJB 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        
        Double charge = null;

        while (true)
        {
            try 
            {
            System.out.println("How much was the food?");
            charge = Double.parseDouble(scanner.nextLine());
            break;
            } 
            catch (NumberFormatException e) 
            {
            System.out.println("Invalid input. Please enter valid numbers.");
            }
        }

        Double tax = (charge * 0.075);
        Double tip = ((tax + charge) * 0.18);
        Double total = (charge + tax + tip);
    


        System.out.println("Subtotal: $" + String.format("%.2f", charge));
        System.out.println("Tax: $" + String.format("%.2f", tax));
        System.out.println("Tip: $" + String.format("%.2f", tip));
        System.out.println("Total: $" + String.format("%.2f", total));


        scanner.close();
    }    
}
