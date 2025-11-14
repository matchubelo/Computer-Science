package Java;

public class testing {
    
    public static void main(String[] args) {

        int temp = 75;
        String choice;
        boolean hasSibling = false;
        
        if (temp < 70) 
        {
           choice = "Indoors"; 
        }
        else 
        { 
           choice = "Outdoors"; 
        }
        if (hasSibling)
        {
           choice += " with sibling";
        }
    System.out.println(choice);
    }
}