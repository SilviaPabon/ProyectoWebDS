/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
import java.util.Iterator;
import java.util.Arrays;
import static java.lang.System.*;

public class List implements ListInterface, Iterable<ListNode> {

    private ListNode inode;
    private int size;

    public ListNode head;
    public ListNode tail;

    /**
     * List
     */
    public List() {
        clear();
    }

    /*
    ok
     */
    public List(Object object) {
        add(object);
    }

    /*
    ok
     */
    @Override
    public boolean isEmpty() {
        return head == null;
    }

    /*
    ok
     */
    @Override
    public int getSize() {
        return size;
    }

    /*
    ok
     */
    @Override
    public void clear() {
        head = null;
        tail = null;
        size = 0;
    }

    /*
    ok
     */
    @Override
    public Object getHead() {
        return head;
    }

    /*
    ok
     */
    @Override
    public Object getTail() {
        return tail;
    }

    /*
    ok
     */
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

    /*
    ok
     */
    @Override
    public boolean add(Object object) {
        return insertHead(object);
    }

    /*
    ok
     */
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
    /*
    ok
     */
    @Override
    public boolean insert(ListNode node, Object object) {
        try {
            if (node.next == null) {
                insertTail(object);
            } else {
                ListNode newNode = new ListNode(object);
                newNode.next = node.next;
                node.next = newNode;
            }
            return true;
        } catch (Exception e) {
            return false;
        }
    }
    /*
    ok
     */
    @Override
    public boolean insertHead(Object object) {
        try {
            if (isEmpty()) {
                head = new ListNode(object);
                tail = head;
            } else {
                head = new ListNode(object, head);
            }
            this.size++;
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    /*
    ok
     */
    @Override
    public boolean insertTail(Object object) {
        try {
            if (isEmpty()) {
                head = new ListNode(object);
                tail = head;
            } 
            else {
                tail.next = new ListNode(object);
                tail = tail.next;
            }
            this.size++;
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    /*
    ok
     */
    @Override
    public boolean remove(ListNode node) {
        if (head != null){
            if (head.next == null){
                clear();
            } 
            else{
            ListNode puntero = head;
            while (puntero.next != node){
                puntero = puntero.next;
            }
            puntero.next = node.next;
            node.next = null;
            }
        }
        size--;
        return true;
    }

    /*
    ok
     */
    @Override
    public boolean remove(Object object) {
        if (head != null){
            if (head.next == null){
                clear();
            } 
            else{
                ListNode node = search(object);
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
        return false;
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
    public Object[] toArray(Object[] object) {
        object = new Object[this.size];
        Iterator<ListNode> i = this.iterator();
        int cont = 0;
        while(i.hasNext() && cont < this.size){
            object[cont]=i.next();
        }
        return new Object[this.size];
    }
    
    
    @Override
    public Object[] toArray(){
        Object[] object;
        object = new Object[this.size];
        Iterator<ListNode> i = this.iterator();
        int cont = 0;
        while(i.hasNext() && cont < this.size){
            object[cont]=i.next();
            cont++;
        }
        return object;
    }
    /*
    ok
     */
    @Override
    public ListNode getBeforeTo(ListNode node) {
        ListNode beforenode = head;
        while (beforenode !=null && beforenode.next!=node){
            beforenode = beforenode.next;
        }
        return beforenode;
    }
    @Override
    public Object getBeforeTo(){
        ListNode beforenode = this.head;
        while (beforenode !=null && beforenode.next!=this.inode){
            beforenode = beforenode.next;
        }
        return beforenode;
    }

    @Override
    public Object getNextTo(ListNode node) {
        Object ob = node.getObject();
        ListNode inode = this.search(ob);
        inode = inode.next;
        return inode;
    }
    @Override
    public Object getNextTo(){
        ListNode temp = this.search(inode);
        inode = temp.next;
        return inode;
    }

    @Override
    public List subList(ListNode from, ListNode to) {
        if (!isEmpty()){
        List subList = new List();
        subList.head = from;
        subList.tail = to;
        ListNode ite = head;
            while (ite.next!=to && ite != ite.next){
                subList.add(ite);
                ite = ite.next;
            }
            return subList;
        }else{
            return null;
        }
    }

    @Override
    public List sortList() {
        List sortList = new List();
        Object[] arreglo = this.toArray();
        Arrays.sort(arreglo);
        int cont = 0;
        while ( cont < arreglo.length){
            sortList.add(arreglo[cont]);
            cont++;
        }
        return sortList;
    }

    @Override
    public Iterator<ListNode> iterator() {
        inode = head;
        return new Iterator<>() {
            @Override
            public boolean hasNext() {
                return inode.next != null;
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

    public void rec(ListNode node) {
        if (node.next != null) {
            rec(node.next);
            // <- ;) ->
        }
        out.println(node.toString());
    }
}
