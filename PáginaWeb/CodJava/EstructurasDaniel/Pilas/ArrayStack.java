/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
import java.util.Arrays;
import java.util.Collections;

public class ArrayStack implements StackInterface {

    private int size;
    private Object[] array;
    private int top;

    public ArrayStack(int size) {
        this.size = size;
        this.array = new Object[(size > 0) ? size : 1];
        clear();
    }

    @Override
    public void clear() {
        for (int i = 0; i < array.length; i++) {
            array[i] = null;
        }
        top = -1;
    }

    @Override
    public boolean isEmpty() {
        return array[top] == null;
    }

    @Override
    public Object peek() {
        return (!isEmpty()) ? array[top] : null;
    }

    @Override
    public Object pop() {
        if (!isEmpty()) {
            Object object = array[top];
            array[top--] = null;
            return object;
        } else {
            return null;
        }
    }

    @Override
    public boolean push(Object object) {
        if (top + 1 < size) {
            try {
                array[++top] = object;
                return true;
            } catch (Exception e) {
                System.out.println(e);
                return false;
            }
        } else {
            return false;
        }
    }

    @Override
    public int size() {
        return top + 1;
    }

    @Override
    public boolean search(Object object) {
        return Arrays.asList(array).contains(object);
    }

    @Override
    public void sort() {
        Arrays.sort(array);
    }

    @Override
    public void reverse() {
        Collections.reverse(Arrays.asList(array));
    }

    @Override
    public String toString() {
        return "ArrayStack{" +
                "size=" + size +
                ", array=" + Arrays.toString(array) +
                ", top=" + top +
                '}';
    }
}
