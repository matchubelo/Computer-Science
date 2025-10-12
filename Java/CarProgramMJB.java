package Java;

public class CarProgramMJB {
    public static void main(String[] args) 
    {
        int yearin = 1997;
        String makein = "Toyota Land Cruiser";
        
        Car car = new Car(yearin, makein);

        car.setspeed(0);
        int acceltimes = 0;
        int braketimes = 0;

        while (acceltimes < 5)
        {
            car.accelerate();
            System.out.println("Your " + car.getyear() + " " + car.getmake() + " is going " + car.getspeed() + " MPH");
            acceltimes = acceltimes + 1;
        }

        System.out.println("");

        while (braketimes < 5)
        {
            car.brake();
            System.out.println("Your " + car.getyear() + " " + car.getmake() + " is going " + car.getspeed() + " MPH");
            braketimes = braketimes + 1;
        }
    }
}
