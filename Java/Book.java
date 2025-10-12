package Java;

public class Book 
{
    private String title;
    private String author;
    private double price;

    public Book()
    {
        title = "";
        author = "";
        price = 0.0;
    }

    public Book(String title, String author, double price)
    {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    public void settitle(String title)
    {
        this.title = title;
    }

    public void setauthor(String author)
    {
        this.author = author;
    }

    public void setprice(double price)
    {
        this.price = price;
    }

    public String gettitle()
    {
        return title;
    }

    public String getauthor()
    {
        return author;
    }

    public double getprice()
    {
        return price;
    }
}
