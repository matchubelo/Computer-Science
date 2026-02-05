package Java;

public class Payroll7 {
	private int[] employeeId = {5658845, 4520125, 7895122, 8777541, 8451277, 1302850, 7580489};
	private int[] hours = new int[7];
	private double[] payRate = new double[7];
	private double[] wages = new double[7];

	public int getEmployeeId(int index) {
		return employeeId[index];
	}

	public int[] getEmployeeIds() {
		return employeeId.clone();
	}

	public int getHours(int index) {
		return hours[index];
	}

	public void setHours(int index, int value) {
		hours[index] = value;
		updateWages(index);
	}

	public double getPayRate(int index) {
		return payRate[index];
	}

	public void setPayRate(int index, double value) {
		payRate[index] = value;
		updateWages(index);
	}

	public double getWages(int index) {
		return wages[index];
	}

	private void updateWages(int index) {
		wages[index] = hours[index] * payRate[index];
	}

	
	public double getGrossPay(int empId) {
		for (int i = 0; i < employeeId.length; i++) {
			if (employeeId[i] == empId) {
				return wages[i];
			}
		}
		throw new IllegalArgumentException("Employee ID not found: " + empId);
	}
}
