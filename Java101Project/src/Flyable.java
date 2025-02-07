public interface Flyable {
    // The difference between an interface a
    // a class can implement multiple interfaces, but only inherit 1 abstract class
    // interfaces groups empty method bodies, whereas an abstract class is more like a skeleton class to inherit from
    // interfaces are used in the case where inheritance doesnt make sense, however there are multiple implementations
    // of classes which share the same function signatures, for example a Flyable (something that can fly)
    // unlike animals which will all have some similar class attributes and methods, which it can then inherit from and
    // implement, a Flyable could be literally anythign that could fly, which doesnt lead to an inheritance pattern

    // an interface is almost like a c .h file, if the file were to be implemented by multiple other files

    // another example of where an interface would be used is for Lists/Set interfaces

    void fly();
    default void land() {
        System.out.println("this object cannot land");
    }
}
