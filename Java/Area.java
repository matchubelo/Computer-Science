package Java;

public class Area 
{

	public static double area(double radius) 
    {
		while (radius < 0) 
        {
			System.out.println("Invalid radius: must be non-negative.");
			return 0.0;
		}
		return Math.PI * radius * radius;
	}

	public static double area(double width, double length) 
    {
		while (width < 0 || length < 0) 
        {
			System.out.println("Invalid width or length: must be non-negative.");
			return 0.0;
		}
		return width * length;
	}


	public static double area(double radius, double height, boolean isCylinder) 
    {
		while (radius < 0 || height < 0) 
        {
			System.out.println("Invalid radius or height: must be non-negative.");
			return 0.0;
		}
		return Math.PI * radius * radius * height;
	}
}