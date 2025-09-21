package Java;

public class EmployeeProgramMJB
{
    public static void main(String[] args)
    {
        EmployeeClassesMJB employee0 = new EmployeeClassesMJB();
        EmployeeClassesMJB employee1 = new EmployeeClassesMJB();
        EmployeeClassesMJB employee2 = new EmployeeClassesMJB();

        employee0.setname("Susan Meyers");
        employee0.setidnumber(47899);
        employee0.setdepartment("Accounting");
        employee0.setposition("Vice President");

        employee1.setname("Mark Jones");
        employee1.setidnumber(39119);
        employee1.setdepartment("IT");
        employee1.setposition("Programmer");

        employee2.setname("Joy Rogers");
        employee2.setidnumber(81774);
        employee2.setdepartment("Manufacturing");
        employee2.setposition("Engineer");

        System.out.println("Name        ID Number       Department      Position");
        System.out.println(employee0.getname() + " " + employee0.getidnumber() + "          " + employee0.getdepartment() + "      " + employee0.getposition());
        System.out.println(employee1.getname() + "   " + employee1.getidnumber() + "          " + employee1.getdepartment() + "              " + employee1.getposition());
        System.out.println(employee2.getname() + "   " + employee2.getidnumber() + "          " + employee2.getdepartment() + "   " + employee2.getposition());
    }
}