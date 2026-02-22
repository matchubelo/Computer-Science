package Java;

import java.util.ArrayList;

public class Practice 
{
    public void sortNames(ArrayList<String> input) 
    {
        input.sort((a, b) -> a.compareTo(b));
    }
}