package Java;
import java.util.Scanner;

public class BoilingPointProgram 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a temperature (F): ");
        double temp = scanner.nextDouble();

        BoilingPoint bp = new BoilingPoint(temp);

        System.out.println();
        System.out.println("At " + temp + "°F:");
        System.out.println("Substances that will freeze at this temperature:");
        boolean anyFreeze = false;
        if (bp.isEthylFreezing()) {
            System.out.println("Ethyl alcohol");
            anyFreeze = true;
        }
        if (bp.isOxygenFreezing()) {
            System.out.println("Oxygen");
            anyFreeze = true;
        }
        if (bp.isWaterFreezing()) {
            System.out.println("Water");
            anyFreeze = true;
        }
        if (!anyFreeze) {
            System.out.println("None");
        }

        System.out.println();
        System.out.println("Substances that will boil at this temperature:");
        boolean anyBoil = false;
        if (bp.isEthylBoiling()) {
            System.out.println("Ethyl alcohol");
            anyBoil = true;
        }
        if (bp.isOxygenBoiling()) {
            System.out.println("Oxygen");
            anyBoil = true;
        }
        if (bp.isWaterBoiling()) {
            System.out.println("Water");
            anyBoil = true;
        }
        if (!anyBoil) {
            System.out.println("None");
        }

        scanner.close();
    }
}
