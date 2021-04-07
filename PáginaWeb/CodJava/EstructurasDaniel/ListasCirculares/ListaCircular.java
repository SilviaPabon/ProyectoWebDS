/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.util.Iterator;
/**
 *
 * @author Daniel
 */
public class ListaCircular implements ListInterface, Iterable<ListNode>{
    public ListNode head;
    public ListNode tail;
    private ListNode inode;
    private int size;
    
    public ListaCircular(){
        clear();
    }
    @Override
    public boolean isEmpty(){
        return head == null;
    }
    @Override
    public int getSize(){
        return size;
    }
    @Override
    public void clear() {
        head = null;
        tail = null;
        size = 0;
    }
    @Override
    public Object getHead() {
        return head;
    }
    @Override
    public Object getTail() {
        return tail;
    }
    @Override
    public boolean insertHead(Object object){
        try {
            if (isEmpty()){
                head = new ListNode(object);
                tail = head;
                tail.setNext(head);
            }else{
                head = new ListNode(object,head);
                tail.setNext(head);
            }
            this.size++;
            return true;
        }catch (Exception e) {
            return false;
        }
    }
    @Override
    public boolean insertTail (Object object){
        try{
            if (isEmpty()){
                head = new ListNode(object);
                tail = head;
                tail.setNext(head);
            }else{
                tail.next = new ListNode(object);
                tail = tail.next;
                tail.setNext(head);
            }
            this.size++;
            return true;
        }catch (Exception e){
            return false;
        }
    }
        @Override
    public boolean add(Object object){
        return insertTail(object);
    }
    @Override
    public ListNode search(Object object) {
        Iterator<ListNode> i = this.iterator();
        ListNode inode;
        while ((inode = i.next()) != null) {
            if (inode.getObject().toString().equals(object.toString())) {
                return inode;
            }
        }
        return null;
    }
    @Override
    public boolean insert(Object ob, Object object) {
        try {
            if (ob != null) {
                ListNode node = this.search(ob);
                if (node != null) {
                    return insert(node, object);
                } else {
                    return false;
                }
            } else {
                return false;
            }
        } catch (Exception e) {
            return false;
        }
    }
    @Override
    public boolean insert(ListNode node, Object object) {
        try {
            if (node.next==head) {
                add(object);
            } else {
                ListNode newNode = new ListNode(object);
                newNode.next = node.next;
                node.next = newNode;
            }
            this.size++;
            return true;
        } catch (Exception e) {
            return false;
        }
        
    }
    @Override
    public boolean remove(ListNode node) {
        if (head != null){
            if (head.next == head){
                clear();
            } 
            else{
            ListNode puntero = head;
            while (puntero.next != node){
                puntero = puntero.next;
            }
            ListNode temp = puntero.next;
            puntero.next = temp.next;
            temp.next = null;
            }
        }
        size--;
        return true;
    }
    
        @Override
    public boolean remove(Object object) {
        if (head != null){
            if (head.next == head){
                clear();
            } 
            else{
                ListNode node = search(object);
                remove (node);
            }
        }
        size--;
        return false;
    }
       /* @Override
    public Object getNextTo(){
    }*/

    @Override
    public Object getNextTo(ListNode node){
        return node.next;
    }
    
    @Override
    public ListNode getBeforeTo(ListNode node) {
        ListNode beforenode = head;
        while (beforenode != null && beforenode.next != node){
            beforenode = beforenode.next;
        }
        return beforenode;
    }
    
    @Override
    public boolean contains(Object object) {
        if (isEmpty()){
            return false;
        } else {
            ListNode node = this.search(object);
            if (node != null){
                return true;
            }else{
                return false;
            }
        }
    }
        @Override
    public Iterator<ListNode> iterator() {
        inode = head;
        return new Iterator<>() {
            @Override
            public boolean hasNext() {
                return inode.next != head;
            }
            @Override
            public ListNode next() {
                if (inode != null) {
                    ListNode tmp = inode;
                    inode = inode.next;
                    return tmp;
                } else {
                    return null;
                }
            }
        };
    }
    
    public ListaCircular sublist (ListNode from, ListNode to){
        if (!isEmpty()){
            ListaCircular sublist = new ListaCircular();
            sublist.head = from;
            sublist.tail = to;
            ListNode ite = head;
            while (ite.next != tail){
                add(ite.next);
            }
        return sublist;
        }else{
            return null;
        }
    }

    @Override
    public Object[] toArray() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public Object[] toArray(Object[] object) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public Object getBeforeTo() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public Object getNextTo() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public ListaCircular subList(ListNode from, ListNode to) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public ListaCircular sortList() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
    
    /*
    @Override
    public Object[] toArray(); ArrayList

    @Override
    public Object[] toArray(Object[] object);

    @Override
    public Object getBeforeTo();

    @Override
    public Object getNextTo();

    @Override
    public ListaCircular sortList();
}
*/