
public class TicketCounter {
    private double ticketPrice;
    private int ticketsSold;
    private double totalRevenue;

    public TicketCounter(double ticketPrice) {
        this.ticketPrice = ticketPrice;
        ticketsSold = 0;
        totalRevenue = 0.0;
    }

    public void sellTickets(int numTickets) {
        ticketsSold += numTickets;
        totalRevenue += numTickets * ticketPrice;
    }

    public double getTotalRevenue() {
        return totalRevenue;
    }

    public int getTicketsSold() {
        return ticketsSold;
    }

    public void applyDiscount(double percent) {
        ticketPrice = ticketPrice * (1 - percent / 100.0);
    }
}