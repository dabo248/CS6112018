package com.dabo;

import java.awt.*;

public class Main {

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
    }
}
