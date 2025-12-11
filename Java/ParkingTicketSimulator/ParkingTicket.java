package Java.ParkingTicketSimulator;

public class ParkingTicket 
{
	private ParkedCar car;
	private PoliceOfficer officer;
	private double fine;
	private int minutesIllegallyParked;

	public ParkingTicket(ParkedCar car, PoliceOfficer officer, int minutesIllegallyParked) 
    {
		this.car = car;
		this.officer = officer;
		this.minutesIllegallyParked = minutesIllegallyParked;
		this.fine = calculateFine(minutesIllegallyParked);
	}

	private double calculateFine(int minutes) 
    {
		int hours = (minutes + 59) / 60;
		if (hours <= 0) return 0.0;
		return 25.0 + (hours - 1) * 10.0;
	}

	public void printTicket() 
    {
		System.out.println("--- Parking Ticket ---");
		System.out.println("Car: " + car.getMake() + " " + car.getModel() + ", " + car.getColor() + ", License: " + car.getLicenseNumber());
		System.out.println("Minutes illegally parked: " + minutesIllegallyParked);
		System.out.println("Fine: $" + fine);
		System.out.println("Officer: " + officer.getName() + ", Badge #: " + officer.getBadgeNumber());
	}
}
