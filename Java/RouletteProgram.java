package Java;
import java.util.Random;

public class RouletteProgram 
{
    public static void main(String[] args) 
    {
        Random random = new Random();
        int pocket = random.nextInt(37);

        RoulettePocket rp = new RoulettePocket(pocket);

        System.out.println("Pocket: " + rp.getNumber() + " " + rp.getPocketColor());
    }
}
