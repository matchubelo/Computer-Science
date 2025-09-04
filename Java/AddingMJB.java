package Java;

import java.util.Scanner;

public class AddingMJB
{
    public static void main(String[] args) 
    {
        // Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        // Prompt for two seperate numbers
        Float num1 = null;
        Float num2 = null;

        while (true) 
        {
            try 
            {
            System.out.println("Enter the First Number");
            num1 = Float.parseFloat(scanner.nextLine());

            System.out.println("Enter the Second Number");
            num2 = Float.parseFloat(scanner.nextLine());

            break; // exit loop if both inputs are valid
            } 
            catch (NumberFormatException e) 
            {
            System.out.println("Invalid input. Please enter valid integers.");
            }
        }

        // Add the two numbers and print out result
        Float sum = num1 + num2;
        System.out.println("The sum of the numbers: " + num1 + ", and " + num2 + ", is " + sum);

        // Close the scanner
        scanner.close();
    }
}