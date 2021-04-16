/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.util.Arrays;
import java.util.Collections;
/**
 *
 * @author Daniel
 */
public class ArrayQueue implements QueueInterface{
    
    private int size;
    private Object[] array;

    public ArrayQueue(int size) {
        this.size = size;
        this.array = new Object[(size > 0) ? size : 1];
        clear();
    }
    
//Funciona
    @Override
    public void clear() {
        for (int i = 0; i < array.length; i++) {
            array[i] = null;
        }
    }
//Funciona
    @Override
    public boolean isEmpty() {
        return array[0] == null;
    }
//Funciona
    @Override
    public Object extract() {
        if (!isEmpty()) {
            Object object = array[0];
            array[0] = null;
            return object;
        } else {
            return null;
        }
    }
//Funciona
    @Override
    public boolean insert(Object object) {
        for (int i=0 ; i < array.length ; i++){
            if (array[i] == null){
                array[i] = object;
                return true;
            }
        }
        return false;
    }
//Funciona
    @Override
    public int size() {
        return array.length;
    }
//Funciona
    @Override
    public boolean search(Object object) {
        return Arrays.asList(array).contains(object);
    }

//Funciona
    @Override
    public void reverse() {
        Collections.reverse(Arrays.asList(array));
    }
    
    @Override
    public void sort() {
        Arrays.sort(array);
    }

    @Override
    public String toString() {
        String arreglo ="Array= ";
        for (int i = 0; i<array.length ; i++){
            arreglo+= array[i] + " ";
        }
        return arreglo;
    }
}
