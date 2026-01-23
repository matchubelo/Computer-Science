package Java;

public class Rainfall 
{
    private double[] data = new double[12];


    public Rainfall(double data[])
    {
        this.data = data;
    }

    public static String month(int n)
    {
        String m = "";
        
        if (n == 0)
        {
            m = "January";
        }
        else if (n == 1)
        {
            m = "February";
        }
        else if (n == 2)
        {
            m = "March";
        }
        else if (n == 3)
        {
            m = "April";
        }
        else if (n == 4)
        {
            m = "May";
        }
        else if (n == 5)
        {
            m = "June";
        }
        else if (n == 6)
        {
            m = "July";
        }
        else if (n == 7)
        {
            m = "August";
        }
        else if (n == 8)
        {
            m = "September";
        }
        else if (n == 9)
        {
            m = "October";
        }
        else if (n == 10)
        {
            m = "November";
        }
        else if (n == 11)
        {
            m = "December";
        }
        return m;
    }

    public double total()
    {
        double sum = 0;
        for (int i = 0; i < data.length; i++) 
        {
            sum += data[i];
        }
        return sum;
    }

    public double average(double sum)
    {
        double avg = sum / 12;
        return avg;
    }

     public String most() {
        int mostIndex = 0;

        for (int i = 1; i < data.length; i++) {
            if (data[i] > data[mostIndex]) {
                mostIndex = i;
            }
        }
        return month(mostIndex);
    }

     public String least() {
        int minIndex = 0;

        for (int i = 1; i < data.length; i++) {
            if (data[i] < data[minIndex]) {
                minIndex = i;
            }
        }
        return month(minIndex);
    }
}