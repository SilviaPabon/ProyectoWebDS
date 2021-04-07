/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.Arrays;
import static java.lang.System.*;
/**
 *
 * @author Daniel
 */
public class ListaDoble {
    
    private int size;
    public ListNode head;
    public ListNode tail;
    
    public ListaDoble(){
        clear();
    }
    
    public ListaDoble(Object object) {
        add(object);
    }
    //Funciona
    public boolean add(Object object) {
        return insertTail(object);
    }
    //Funciona
    public boolean insertHead(Object object) {
            if (isEmpty()) {
                head = new ListNode(object);
                tail = head;
            } else {
                head = new ListNode(object,head,null);
                head.siguiente.anterior = head;
            }
            this.size++;
            return true;
    }
    //Funciona
    public boolean insertTail(Object object) {
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
    public boolean insert(ListNode node, Object object){
        try{
            if (node.siguiente==null){
                insertTail(object);
            }else{
                if (node.anterior == null){
                    insertHead(object);
                }else{
                    ListNode nuevoNodo = new ListNode(object);
                    nuevoNodo.siguiente = node.siguiente;
                    node.siguiente.anterior = nuevoNodo;
                    node.siguiente = nuevoNodo;
                    nuevoNodo.anterior = node;
                    size++;
                }
                
            }
            return true;
        } catch(Exception e){
            return false;
        }
    }
    //Funciona
    public boolean insert(Object ob, Object object){
        try{
        if (ob != null){
            ListNode node = search(ob);
            if (node!=null){
                return insert(node,object);
            }else{
                return false;
            }
        }else{
            return false;
        }
        }catch (Exception e){
            return false;
        }
    }
    
    //Funciona
    public boolean isEmpty() {
        return head == null;
    }
    //Funciona
    public void clear() {
        head = null;
        tail = null;
        size = 0;
    }
    //Funciona
    public int getSize() {
        return size;
    }
    //Funciona
    public Object getHead() {
        return head.objeto;
    }
    //Funciona
    public Object getTail() {
        return tail.objeto;
    }
    //Funciona
    public boolean remove(ListNode node){
        if (head != null){
            if (head.siguiente == null){
                clear();
            }else{
                ListNode aux = head;
                while (aux.siguiente != node){
                    aux = aux.siguiente;
                }
                aux.siguiente = node.siguiente;
                node.siguiente.anterior = aux;
                node.siguiente = null;
                node.anterior = null;
            }
        }
        size--;
        return true;
    }
    //Funciona
    public boolean remove(Object objeto){
        if (head!= null){
            if (head.siguiente == null){
                clear();
            }else{
                ListNode aux = head;
                ListNode node = search(objeto);
                while (aux.siguiente != node){
                    aux = aux.siguiente;
                }
                aux.siguiente = node.siguiente;
                node.siguiente.anterior = aux;
                node.siguiente = null;
                node.anterior = null;
            }
        }
        size--;
        return true;
    }
    //Funciona
    public ListNode search(Object object){
        ListNode ite = head;
        while(ite!=null && ite.objeto!=object){
            ite = ite.siguiente;
        }
        if (ite.objeto == object){
            return ite;
        }else{
            return null;
        }
    }
    //Funciona
    public boolean contains(Object object){
        if (isEmpty()){
            return false;
        }else{
            ListNode node = search(object);
            if (node != null && node.objeto != null){
                return true;
            }else{
                return false;
            }
        }
    }
    
    /*public Object getBeforeTo(){
        
    }*/

    public Object getBeforeTo(ListNode node){
        ListNode before = node.anterior;
        if (before == null){
            return null;
        }else{
            return before.objeto;
        }
        
    }

    /*public Object getNextTo(){
    }*/

    public Object getNextTo(ListNode node){
        ListNode next = node.siguiente;
        if (next == null){
            return null;
        }else{
            return next.objeto;
        }
        
    }
    //Funciona
    public ListaDoble subList(ListNode from, ListNode to){
        ListaDoble sublist = new ListaDoble();
        ListNode ite = from;
        while(ite != to.siguiente){
            sublist.add(ite.objeto);
            ite = ite.siguiente;
        }
        return sublist;
    }
    //Funciona
    public Object[] toArray(){
        Object[] objetos = new Object[size];
        ListNode ite = head;
        int cont = 0;
        while (ite != null){
            objetos[cont]=ite.objeto;
            ite = ite.siguiente;
            cont++;
        }
        return objetos;
    }
    //Funciona
    @Override
    public String toString(){
        String lista="";
        ListNode ite = head;
        while(ite.siguiente != null){
            lista += " ListNode{objeto="+ite.objeto+"},siguiente=";
            ite = ite.siguiente;
        }
        lista += " ListNode{objeto="+tail.objeto+'}';
        return lista;
    }

    
    
    /*

    public Object[] toArray(Object[] object);

    public List sortList();
    */
}
