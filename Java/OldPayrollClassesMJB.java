package Java;

public class OldPayrollClassesMJB 
{
    private String name;
    private double hourly_rate;
    private double hours_work;

    public void setname(String namein)
    {
        name = namein;
    }

    public void sethourlyrate (double ratein)
    {
        hourly_rate = ratein;
    }
    
    public void sethours (double hoursin)
    {
        hours_work = hoursin;
    }

    public String getname()
    {
        return name;
    }

    public double getrate()
    {
        return hourly_rate;
    }

    public double gethours()
    {
        return hours_work;
    }

    public double getgrosspay()
    {
        return (hours_work * hourly_rate);
    }   

}
