import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // type psvm <tab> to autogenerate the line above
        basics();
        inheritanceExample();
        interfaceExample();
    }
    private static void inheritanceExample() {
//        Animal animal = new Animal("jeff", 10);
        Dog coco = new Dog("coco", 4, "schnauzer");
        coco.displayInfo();
        coco.makeSound();

    }

    public static void interfaceExample() {
        Flyable myBird = new Bird("birdy");
//        myBird.setName("bird");
        Bird otherBird = new Bird("brid");
        otherBird.setName("bird");
        otherBird.fly();

    }

    private static void basics() {
        // type fori <tab> to autogenerate a loop
        for (int i = 0; i < 5; i++) {
            // type sout <tab> to autogenerate the line below
            System.out.println(i);
        }

        // i wont bore you with the rest of the loops
        // although foreach is very useful

        // STRINGS

        String str = "Hello";
        str = str + " World"; // Creates a new String object
        System.out.println("String: " + str);

        // strings are immutable fixed length character arrays
        // since under the hood, a String in java is a fixed sice character array, it means that to concatonate 2
        // strings, we end up creating a new array

        // we can use string builder since it has an internal variable sized array, where lookup and appending are
        // O(n), with space being O(n) too.
        StringBuilder sb = new StringBuilder(str);

        // Append a string
        String stringToAppend = "!!!";
        sb.append(stringToAppend);
        System.out.println("After appending: " + sb);

        // Delete a portion of the StringBuilder
        sb.delete(5, 11); // Deletes " World"
        System.out.println("After deletion: " + sb);

        // Insert a string at a specific position
        String stringToInsert = " Java";
        sb.insert(5, stringToInsert); // Inserts " Java" at position 5
        System.out.println("After insertion: " + sb);

        // Reverse the StringBuilder and convert back to String
        sb.reverse();
        String modifiedString = sb.toString();
        System.out.println("modified string: " + modifiedString);

        // LISTS

        // like with strings, lists also have their literals, and their class interpretations
        // we could use int[] or ArrayList<Int> or List<Int>
        int[] arr = {1, 2, 3, 4, 5};

        // Append (requires new array)
        int[] appendedArr = Arrays.copyOf(arr, arr.length + 1);
        appendedArr[arr.length] = 6;

        // Pop (reduce size by one)
        int[] poppedArr = Arrays.copyOf(arr, arr.length - 1);

        // Delete (remove element at index 2)
        int[] deletedArr = new int[arr.length - 1];
        for (int i = 0, j = 0; i < arr.length; i++) {
            if (i != 2) {
                deletedArr[j++] = arr[i];
            }
        }

        // Insert (add element at index 2)
        int[] insertedArr = new int[arr.length + 1];
        for (int i = 0, j = 0; i < arr.length; i++) {
            if (i == 2) {
                insertedArr[j++] = 99; // Inserted element
            }
            insertedArr[j++] = arr[i];
        }

        // Range (sub-array from index 1 to 3)
        int[] rangeArr = Arrays.copyOfRange(arr, 1, 4);

        // Printing results
        System.out.println("Appended: " + Arrays.toString(appendedArr));
        System.out.println("Popped: " + Arrays.toString(poppedArr));
        System.out.println("Deleted: " + Arrays.toString(deletedArr));
        System.out.println("Inserted: " + Arrays.toString(insertedArr));
        System.out.println("Range: " + Arrays.toString(rangeArr));


        // Or we could use a List

        // ArrayList is an implementation of the List interface.
        ArrayList<Integer> list = new ArrayList<Integer>(List.of(1, 2, 3, 4, 5));

        // Append
        list.add(6);

        // Pop (remove last element)
        list.remove(list.size() - 1);

        // Delete (remove element at index 2)
        list.remove(2);

        // Insert (add element at index 2)
        list.add(2, 99);

        // Range (sub-list from index 1 to 3)
        List<Integer> rangeList = list.subList(1, 4);

        for (int i = 0; i < list.size(); i++) {
            int someint = list.get(i);
        }

        // Printing results
        System.out.println("ArrayList: " + list);
        System.out.println("Range: " + rangeList);

    }
}