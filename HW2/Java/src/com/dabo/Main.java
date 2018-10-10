package com.dabo;

import java.awt.*;

public class Main {

    public static int sum_for(int n) {
        int i = 0, sum = 0;
        for (i = 0; i <= n; i++) {
            sum += i;
        }
        return sum;
    }

    public static int sum_while(int n) {
        int i = 0, sum = 0;
        while (i <= n) {
            sum += i;
            i++;
        }
        return sum;
    }

    public static int fact(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * fact(n - 1);
        }
    }

    public static int smallest_tail_recursive_function(int n) {
        if (n == 0) {
            return 5;
        } else {
            return smallest_tail_recursive_function(n - 1);
        }
    }

    public static void main(String[] args) {
	    // write your code here
        System.out.println("Hello World");

        // question 1, a
        Circle circle = new Circle();
        circle.draw();
        circle.draw(Color.black);

        ColoredCircle colored_circle = new ColoredCircle();
        colored_circle.draw();

        // question 1, b
        // colored_circle = (ColoredCircle) circle;

        // question 1, c
        circle = colored_circle;
        circle.draw();

        // question 2, c
        int i = 5;
        i = i + 5;

        // question 2, e
        int factorial_result = fact(7);

        System.out.println(factorial_result);

        // question 2, f
        int tail_recursive_result = smallest_tail_recursive_function(10);

        System.out.println(tail_recursive_result);
    }
}
