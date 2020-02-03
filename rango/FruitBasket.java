import java.util.*;

/**
 * @param args
 */

public class FruitBasket {
	public static void main(String[] args) {
		Set<String> basket = new TreeSet<String>();
		for (String a : args)
			basket.add(a);
		for (String f : basket)
			System.out.println("  " + f);
		if (!basket.contains("orange"))
			System.out.println("No orange!");
	}
}
