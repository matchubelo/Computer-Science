package Java;

public class CarClassesMJB 
{
    private int year;
    private String make;
    private int speed;

    public void setyear(int yearin)
    {
        year = yearin;
    }

    public void setmake(String makein)
    {
        make = makein;
    }

    public void setspeed(int speedin)
    {
        speed = speedin;
    }

    public int getyear()
    {
        return year;
    }

    public String getmake()
    {
        return make;
    }

    public int getspeed()
    {
        return speed;
    }

    public void brake()
    {
        setspeed(speed - 5);
    }

    public void accelerate()
    {
        setspeed(speed + 5);
    }

    
}
