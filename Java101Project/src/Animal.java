public abstract class Animal {
    // this is how we declare class variables. they can be public private or protected
    // public gives the variable scope of the whole project
    // protected gives the variable scope of the class and anything that inherits or interfaces it
    // private gives the variable scope of the class and only the class its declared in
    protected String name;
    private int age;
    // here we have an example of a static attribute. this means that this variable belongs to the class, not the
    // instantiated object of the class, so there is only ever 1 numAnimals variable, no matter how many times the class
    // is inherited from and instantiated. for example we can use this to count the number of animals we have instantiated
    private static int numAnimalsCreated = 0;

    // the constructor of the class (__init__() in python) is written as below
    public Animal(String name, int age) {
        // this = self in python
        this.name = name;
        this.age = age;
        // incrementing the number of animals we have instantiated
        numAnimalsCreated++;
    }

    protected int getAge() {
        // notice how we dont have to use this.age. class variables dont have name space priority though so be careful
        // class variables are purple, non-class variables are white (default theme)
        return age;
    }

    protected void setAge(int age) { this.age = age; }

    // this is an abstract method, meaning that any class inheriting this class has to implement the method
    public abstract void makeSound();
}

