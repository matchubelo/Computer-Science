package Java;

import java.util.ArrayList;

public class PracticeDriver {
	public static void main(String[] args) {
		Practice practice = new Practice();
		ArrayList<String> testNames = new ArrayList<>();
		testNames.add("Zoe");
		testNames.add("Anna");
		testNames.add("Mike");
		testNames.add("Beth");

		System.out.println("Before sorting: " + testNames);
		practice.sortNames(testNames);
		System.out.println("After sorting:  " + testNames);
	}
}
