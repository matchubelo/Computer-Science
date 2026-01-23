package Java;
import java.util.*;

public class RainfallMJB 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        double[] data = new double[12];

        for (int count = 0; count < data.length; count++)
        {
            try 
            {
                System.out.println("Enter today's rainfall");
                data[count] = scanner.nextDouble();
            } 
            catch (InputMismatchException e) 
            {
                System.out.println("Invalid input. Please enter a number.");
                scanner.nextLine();
                count--;
            }
        }
        scanner.close();
        
        Rainfall rain = new Rainfall(data);

        System.out.println("Total Rainfall: " + rain.total() + "in.");
        System.out.println("Average Rainfall: " + rain.average(rain.total()) + "in/month");
        System.out.println("Month With the Most Rainfall: " + rain.most());
        System.out.println("Month With the Least Rainfall: " + rain.least());
    }
}