public class ParserDemo {

	private static String file1 = "./src/res/parser_test.jay";

	public static void main(String[] args) {

		System.out.println(file1);

		TokenStream tStream = new TokenStream(file1);
		ConcreteSyntax cSyntax = new ConcreteSyntax(tStream);
		Program p = cSyntax.program();

		System.out.println(p.display());
	}

}
