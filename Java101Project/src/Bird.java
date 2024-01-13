public class Bird implements Flyable {
    // to implement an interface, we implement it
    // here we override the methods
    private String name;
    public Bird(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public void fly() {
        System.out.println("this bird is flying");
    }
    @Override
    public void land() {
        System.out.println("this bird has landed");
    }
}
