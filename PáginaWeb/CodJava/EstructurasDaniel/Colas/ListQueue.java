/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
public class ListQueue implements QueueInterface {
    
        private int size;
        public ListNode head;
        public ListNode tail;
      
        public ListQueue(){
            clear();
        }
//Funciona
    @Override
    public void clear() {
        
        head=null;
        tail=null;
        size=0;
        
        
    }
//Funciona
    @Override
    public boolean isEmpty() {
        
        return head == null;
        
    }
//Funciona
    @Override
    public Object extract() {
        ListNode primero = head;
        head = primero.siguiente;
        head.anterior = null;
        return primero.objeto;
    }
//Funciona
    @Override
    public boolean insert(Object object) {
        if (isEmpty()) {
                head = new ListNode(object);
                tail = head;
            }else {
                tail = new ListNode(object,null,tail);
                tail.anterior.siguiente = tail;
            }
            size++;
            return true;
    }
//Funciona
    @Override
    public int size() {
        
        return size;
        
    }
//Funciona
    @Override
    public boolean search(Object object) {
        try {
        ListNode ite = head;
        while(ite!=null && ite.objeto !=object){
            ite = ite.siguiente;
        }
        if (ite.objeto == object){
            return true;
        }
        else{
            return false;
        }    
        } catch (Exception e) {
            return false;
        }
    }

    @Override
    public void sort() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void reverse() {
        ListNode temp = tail;
        tail = head;
        head = temp;
    }
    
//Funciona
    @Override
    public String toString(){
        String lista="ListQueue= ";
        ListNode ite = head;
        while(ite != null){
            lista += "Object "+ite.objeto +" ";
            ite = ite.siguiente;
        }
        return lista;
    }   
}

