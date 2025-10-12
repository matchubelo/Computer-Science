package Java;
import java.util.Scanner;

public class BookProgramMJB 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        // Book 1: Using no-argument constructor and setters with user input
        Book book1 = new Book();
        System.out.print("Enter title for Book 1: ");
        book1.settitle(scanner.nextLine());
        System.out.print("Enter author for Book 1: ");
        book1.setauthor(scanner.nextLine());
        System.out.print("Enter price for Book 1: ");
        book1.setprice(scanner.nextDouble());
        scanner.nextLine(); // consume newline

        // Book 2: Using constructor with arguments from user input
        System.out.print("Enter title for Book 2: ");
        String title2 = scanner.nextLine();
        System.out.print("Enter author for Book 2: ");
        String author2 = scanner.nextLine();
        System.out.print("Enter price for Book 2: ");
        double price2 = scanner.nextDouble();
        scanner.nextLine(); // consume newline
        Book book2 = new Book(title2, author2, price2);

        // Book 3: Using no-argument constructor and setters with user input
        Book book3 = new Book();
        System.out.print("Enter title for Book 3: ");
        book3.settitle(scanner.nextLine());
        System.out.print("Enter author for Book 3: ");
        book3.setauthor(scanner.nextLine());
        System.out.print("Enter price for Book 3: ");
        book3.setprice(scanner.nextDouble());

        // Display book info
        System.out.println("\nBook 1: " + book1.gettitle() + " by " + book1.getauthor() + " ($" + book1.getprice() + ")");
        System.out.println("Book 2: " + book2.gettitle() + " by " + book2.getauthor() + " ($" + book2.getprice() + ")");
        System.out.println("Book 3: " + book3.gettitle() + " by " + book3.getauthor() + " ($" + book3.getprice() + ")");

        scanner.close();
    }
}
