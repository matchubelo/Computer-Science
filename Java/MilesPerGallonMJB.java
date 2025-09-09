package Java;
import java.util.Scanner;
public class MilesPerGallonMJB 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        
        Float milesdriven = null;
        Float gallons = null;

        while (true)
        {
            try 
            {
            System.out.println("How many miles did you drive?");
            milesdriven = Float.parseFloat(scanner.nextLine());

            System.out.println("How many gallons of fuel did you use?");
            gallons = Float.parseFloat(scanner.nextLine());
            break;
            } 
            catch (NumberFormatException e) 
            {
            System.out.println("Invalid input. Please enter valid numbers.");
            }
        }

        Float milespergallon = (milesdriven / gallons);

        System.out.println("The Gas Mileage for driving " + milesdriven + " miles on " + gallons +  " of fuel is: " + milespergallon + " Miles/Gallon");
        
        scanner.close();
    }
}
