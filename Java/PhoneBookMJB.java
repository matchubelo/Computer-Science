package Java;

import java.util.ArrayList;

public class PhoneBookMJB {
    public static void main(String[] args) {
        ArrayList<PhoneBookEntry> phoneBook = new ArrayList<PhoneBookEntry>();

        // Add at least five entries
        phoneBook.add(new PhoneBookEntry("Kingswood Oxford", "860-233-9631"));
        phoneBook.add(new PhoneBookEntry("George Washington University", "202-994-1000"));
        phoneBook.add(new PhoneBookEntry("Matt", "860-839-0000"));
        phoneBook.add(new PhoneBookEntry("Dom Brunalli", "860-555-4321"));
        phoneBook.add(new PhoneBookEntry("AP CSA", "202-555-0000"));

        // Display all entries
        for (PhoneBookEntry entry : phoneBook) {
            System.out.println(entry);
        }
    }
}
