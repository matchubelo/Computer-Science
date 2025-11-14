package Java;

public class RoulettePocket 
{
    private int number;

    public RoulettePocket(int number) 
    {
        this.number = number;
    }

    public int getNumber() 
    {
        return number;
    }

    public String getPocketColor() 
    {
        if (number == 0) return "Green";

        if (number >= 1 && number <= 10) {
            return (number % 2 != 0) ? "Red" : "Black";
        } else if (number >= 11 && number <= 18) {
            return (number % 2 != 0) ? "Black" : "Red";
        } else if (number >= 19 && number <= 28) {
            return (number % 2 != 0) ? "Red" : "Black";
        } else if (number >= 29 && number <= 36) {
            return (number % 2 != 0) ? "Black" : "Red";
        } else {
            return "Invalid";
        }
    }
}
