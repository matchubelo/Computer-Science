package Java.ParkingTicketSimulator;

public class ParkingMeter 
{
	private int minutesPurchased;

	public ParkingMeter(int minutesPurchased) 
    {
		this.minutesPurchased = minutesPurchased;
	}

	public int getMinutesPurchased() 
    { 
        return minutesPurchased; 
    }
}
