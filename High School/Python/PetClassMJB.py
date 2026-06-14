class Pet:
    def __init__(self, name='', animal_type='', age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
    
# Main program
def main():
    # Create a Pet object
    pet = Pet()

    # Get pet details from user
    name = input("Enter the pet's name: ")
    animal_type = input("Enter the type of animal: ")
    age = int(input("Enter the pet's age (years): "))

    # Set pet details
    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    # Display pet details
    print("\nPet Details:")
    print("\nName:", pet.get_name())
    print("Type:", pet.get_animal_type())
    print("Age:", pet.get_age(), "years old")

main()
