/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
public interface StackInterface {

    public void clear();

    public boolean isEmpty();

    public Object peek();

    public Object pop();

    public boolean push(Object object);

    public int size();

    public boolean search(Object object);

    public void sort();

    public void reverse();

    public String toString();

}
