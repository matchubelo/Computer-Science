package Java;

import java.util.Scanner;

public class AreaProgramMJB {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Circle area
        System.out.print("Enter radius for circle: ");
        double circleRadius = sc.nextDouble();
        double circleArea = Area.area(circleRadius);
        System.out.println("Area of circle (r=" + circleRadius + "): " + circleArea);

        // Rectangle area
        System.out.print("Enter width for rectangle: ");
        double rectWidth = sc.nextDouble();
        System.out.print("Enter length for rectangle: ");
        double rectLength = sc.nextDouble();
        double rectArea = Area.area(rectWidth, rectLength);
        System.out.println("Area of rectangle (" + rectWidth + " x " + rectLength + "): " + rectArea);

        // Cylinder area (volume-like)
        System.out.print("Enter radius for cylinder: ");
        double cylRadius = sc.nextDouble();
        System.out.print("Enter height for cylinder: ");
        double cylHeight = sc.nextDouble();
        double cylArea = Area.area(cylRadius, cylHeight, true);
        System.out.println("Area of cylinder (r=" + cylRadius + ", h=" + cylHeight + "): " + cylArea);

        sc.close();
    }
}
