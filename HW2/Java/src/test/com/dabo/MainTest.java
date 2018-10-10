package test.com.dabo;

import main.com.dabo.Main;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

/**
 * Created by D4VE on 10/10/18.
 */
public class MainTest {

    @Test
    public void recPowHandleAllTypesOfInput() {
        Main tester = new Main();

        try {
            tester.recPow(-10);
            fail("Expected an IllegalArgumentException to be thrown");
        } catch (IllegalArgumentException e) {
            assertEquals("n has to be >= 0 and <= 30", e.getMessage());
        }

        try {
            tester.recPow(42);
            fail("Expected an IllegalArgumentException to be thrown");
        } catch (IllegalArgumentException e) {
            assertEquals("n has to be >= 0 and <= 30", e.getMessage());
        }

        assertEquals(1, tester.recPow(0), "2^0 must be 1");
        assertEquals(1024, tester.recPow(10), "2^10 must be 1024");
    }
}