/**
 * @author Christelle
 * 
 */
public class ScannerDemo {

	private static String file1 = "./src/res/parser_test.jay";
	private static int counter = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(file1);

		System.out.println(file1);

		while (!ts.isEndofFile()) {
			// System.out.println("Scanning..");
			Token t = ts.nextToken();
			System.out.println(counter + " - " + t.toString());
			counter++;
		}

		System.out.println("Finished execution.");
	}
}
