package Java;

public class LandCalculationMJB 
{
    public static void main(String[] args) 
    {
        Integer acresqft = 43560;
        Integer tractsqft = 389767;

        Integer tractacres = tractsqft / acresqft;
        System.out.println("The tract is " + tractacres + " acres.");

    }    
}