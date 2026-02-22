package Java;

public class PhoneBookEntry {
    private String name;
    private String phoneNumber;

    // Constructor
    public PhoneBookEntry(String name, String phoneNumber) {
        this.name = name;
        this.phoneNumber = phoneNumber;
    }

    // Accessor for name
    public String getName() {
        return name;
    }

    // Mutator for name
    public void setName(String name) {
        this.name = name;
    }

    // Accessor for phoneNumber
    public String getPhoneNumber() {
        return phoneNumber;
    }

    // Mutator for phoneNumber
    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    // toString method for display
    public String toString() {
        return "Name: " + name + ", Phone Number: " + phoneNumber;
    }
}
