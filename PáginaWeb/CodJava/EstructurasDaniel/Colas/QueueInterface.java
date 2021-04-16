/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
public interface QueueInterface {
    public void clear();
    
    public boolean isEmpty();
    
    public Object extract();
    
    public boolean insert(Object object);
    
    public int size();
    
    public boolean search(Object object);
    
    public void sort();
    
    public void reverse();
    
    public String toString();
}
