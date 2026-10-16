/*
Once you have designed the class, design a program that creates an object of the class and
prompts the user to enter the name, type, and age of his or her pet. This data should be
stored in the object. Use the object’s accessor methods to retrieve the pet’s name, type, and
age and display this data on the screen.
 */
import java.util.*;

public class PetProgram {
    public static void main(String[] args) 
    {
        Pet che = new Pet();
        Scanner scanner = new Scanner(System.in);

        String name;
        String type;
        int age;

        System.out.println("What is the name of your pet?");
        name = scanner.nextLine();
        che.setName(name);

        System.out.println("What type of Pet is it?");
        type = scanner.nextLine();
        che.setType(type);   
        

        while (true)
        {
            try 
            {
            System.out.println("What age is the pet?");
            age = Integer.parseInt(scanner.nextLine());
            break;
            } 
            catch (NumberFormatException e) 
            {
            System.out.println("Invalid input. Please enter valid numbers.");
            }
        }
        che.setAge(age);

        System.out.println("Pet's Name: " + che.getName());
        System.out.println("Pet Type: " + che.getType());
        System.out.println("Pet's Age: " + che.getAge());
        scanner.close();
    }
    
}
