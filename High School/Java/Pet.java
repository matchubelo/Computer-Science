/*
Pet Class
Design a class named Pet, which should have the following fields:
● name. The name field holds the name of a pet.
● type. The type field holds the type of animal that a pet is. Example values are “Dog”,
“Cat”, and “Bird”.
● age. The age field holds the pet’s age.
The Pet class should also have the following methods:
● setName. The setName method stores a value in the name field.
● setType. The setType method stores a value in the type field.

Programming Challenges 191

● setAge. The setAge method stores a value in the age field.
● getName. The getName method returns the value of the name field.
● gettype. The getType method returns the value of the type field.
● getAge. The getAge method returns the value of the age field.
Once you have designed the class, design a program that creates an object of the class and
prompts the user to enter the name, type, and age of his or her pet. This data should be
stored in the object. Use the object’s accessor methods to retrieve the pet’s name, type, and
age and display this data on the screen.
*/


public class Pet 
{
    private int age;    
    private String type;   
    private String name;
    
    
    public void setAge(int age)
    {
        this.age = age;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public void setType(String type)
    {
        this.type = type;
    }

    public int getAge()
    {
        return age;
    }

    public String getType()
    {
        return type;
    }

    public String getName()
    {
        return name;
    }

}

