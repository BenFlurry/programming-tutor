public class Dog extends Animal {
    // if a variable is set once, and never changed it can be set to final (constant)
    private final String breed;


    public Dog(String name, int age, String breed) {
        // initailise the name and age based off of the abstract class
        super(name, age);
        // initialise the varaible unique to this class
        this.breed = breed;
    }

    public void makeSound() {
        System.out.println(name + " says Woof!");
    }

    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + getAge() + ", Breed: " + breed);
    }
}

