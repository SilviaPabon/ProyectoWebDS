/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
public class ListNode {
    public Object objeto;
    public ListNode siguiente;
    public ListNode anterior;
    
    public ListNode() {
        this.objeto = null;
        this.siguiente = null;
        this.anterior = null;
    }
    public ListNode(Object objeto) {
        this.objeto = objeto;
        this.siguiente = null;
        this.anterior = null;
    }
    
    public ListNode(Object objeto, ListNode siguiente, ListNode anterior) {
        this.objeto = objeto;
        this.siguiente = siguiente;
        this.anterior = anterior;
    }
    
    public Object getObject() {
        return objeto;
    }
    
    public void setObject(Object objeto) {
        this.objeto = objeto;
    }
    
    public boolean isEquals(Object objeto) {
        if (this.getObject().toString().equals(objeto.toString())) {
            return true;
        }
        return false;
    }
    
    public boolean isEquals(ListNode node) {
        if (this.toString().equals(node.toString())) {
            return true;
        }
        return false;
    }
    
    @Override
    public String toString() {
        return "ListNode{" +
                "objeto=" + objeto +
                ", anterior=" + anterior +
                ", siguiente=" + siguiente +
                '}';
    }
}
