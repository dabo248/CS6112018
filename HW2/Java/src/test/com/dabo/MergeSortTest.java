package test.com.dabo;

import main.com.dabo.MergeSort;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

/**
 * Created by D4VE on 10/10/18.
 */
public class MergeSortTest {

    @Test
    public void mergeSortHandleAllTypesOfInput() {
        // normal list
        int[] array = {5, 9, 7, 129, 123, -6, 0};
        MergeSort.mergeSort(array);

        assertArrayEquals(new int[] {-6, 0, 5, 7, 9, 123, 129}, array,
                "Sorted int array must be {-6, 0, 5, 7, 9, 123, 129}");

        // empty list
        array = new int[] {};
        MergeSort.mergeSort(array);

        assertArrayEquals(new int[] {}, array,
                "Nothing happens with an empty array");

        // list containing one value
        array = new int[] {4};
        MergeSort.mergeSort(array);

        assertArrayEquals(new int[] {4}, array,
                "Nothing happens with an array containing only one value");
    }
}