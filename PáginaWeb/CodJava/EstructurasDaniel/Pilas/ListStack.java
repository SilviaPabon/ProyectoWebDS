
import java.util.Arrays;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
public class ListStack implements StackInterface{
    
    
        private int size;
        private ListNode top;
        public ListNode head;
        public ListNode tail;
        
        public ListStack(){
            clear();
        }
    @Override
        public void clear() {
        head = null;
        tail = null;
        top = null;
        size = 0;
        }
    @Override
        public boolean isEmpty() {
        return tail == null;
    }
    @Override
        public Object peek() {
        return tail;
    }
    @Override
        public Object pop(){
            Object pop = peek();
            remove();
            return pop;
        }
    @Override
        public boolean push(Object object) {
        return insertTail(object);
    }
        
        public boolean insertTail(Object object) {
        try {
            if (isEmpty()) {
                head = new ListNode(object);
                tail = head;
            } 
            else {
                tail.next = new ListNode(object);
                tail = tail.next;
                top = tail;
            }
            size++;
            return true;
        } catch (Exception e) {
            return false;
        }
    }
        
        public boolean remove() {
        if (head != null){
            if (head.next == null){
                clear();
            } 
            else
            {
                ListNode temp = tail;
                tail.next = null;
                tail = temp;
            }
        }
        size--;
        return true;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean search(Object object) {
        ListNode ite = top;
        while(ite!=null && ite.object !=object){
            ite = ite.next;
        }
        if (ite.object == object){
            return true;
        }
        else{
            return false;
        }
    }

    @Override 
    public void sort() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    public void reverse(ListStack normal) {
        ListStack reverse = new ListStack();
        while (normal.size > 0){
            reverse.push(normal.pop());
        }
        normal = reverse;
    }

    @Override
    public void reverse() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

}
