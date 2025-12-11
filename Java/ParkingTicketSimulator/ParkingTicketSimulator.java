package Java.ParkingTicketSimulator;

public class ParkingTicketSimulator {
	public static void main(String[] args) 
    {

		ParkedCar car = new ParkedCar("Lexus", "RX350", "Tan", "342XBL", 120);


		ParkingMeter meter = new ParkingMeter(60);


		PoliceOfficer officer = new PoliceOfficer("Mike Ligon", "6741");


		ParkingTicket ticket = officer.inspectCar(car, meter);

		if (ticket != null) 
        {
			ticket.printTicket();
		} 
        
        else 
        {
			System.out.println("No ticket issued. Car is legally parked.");
		}
	}
}
