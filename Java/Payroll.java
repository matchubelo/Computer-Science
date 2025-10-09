package Java;

public class Payroll
{
    private String name;
    private int idnumber;
    private double hourly_rate;
    private double hours_work;

    public void setname(String namein)
    {
        name = namein;
    }

    public void setidnumber(int idnumberin)
    {
        idnumber = idnumberin;
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

    public int getidnumber()
    {
        return idnumber;
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
        if (hours_work > 40)
        {
           double othours = hours_work - 40;
           double otrate = hourly_rate * 1.5;
           double otpay = othours * otrate;
           double regularpay = hours_work * hourly_rate;
           return(regularpay + otpay);
        }
        
        else 
        {
            return(hours_work * hourly_rate);
        }
    }
        
}   