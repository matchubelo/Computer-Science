package Java.ParkingTicketSimulator;

public class PoliceOfficer 
{
	private String name;
	private String badgeNumber;

	public PoliceOfficer(String name, String badgeNumber) 
    {
		this.name = name;
		this.badgeNumber = badgeNumber;
	}

	public String getName() 
    { 
        return name; 

    }
	public String getBadgeNumber() 
    { 
        return badgeNumber; 
    }

	public ParkingTicket inspectCar(ParkedCar car, ParkingMeter meter) {
		int minutesOver = car.getMinutesParked() - meter.getMinutesPurchased();
		if (minutesOver > 0) 
        {
			return new ParkingTicket(car, this, minutesOver);
		} 
        
        else 
        {
			return null;
		}
	}
}
