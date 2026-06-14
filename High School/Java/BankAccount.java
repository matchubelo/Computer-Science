
public class BankAccount {
    private double balance;
    private String accountHolderName;

    public BankAccount(String name, double startingBalance) {
        accountHolderName = name;
        balance = startingBalance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }

    public double getBalance() {
        return balance;
    }

    public void transferTo(BankAccount other, double amount) {
        if (amount <= balance) {
            balance -= amount;
            other.deposit(amount);
        }
    }
}