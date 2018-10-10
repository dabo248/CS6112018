package com.dabo;

import java.awt.*;

/**
 * Created by D4VE on 8/10/18.
 */
public class Circle{
    public double center_x, center_y;
    public double radius;

    public void draw() {
        // (1) method to draw circle on the screen
        System.out.println("> draw a circle");
    }

    public void draw(Color color) {
        // (2) method to draw circle on the screen with a
        // given color
        System.out.println("> draw a circle with " + color);
    }
}