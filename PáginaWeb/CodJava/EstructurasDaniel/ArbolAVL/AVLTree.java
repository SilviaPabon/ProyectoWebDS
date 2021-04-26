/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
public class AVLTree {
    public Node raiz;
    public AVLTree(){
        raiz = null;
    }
    public Node search(int object, Node r){
        if (r == null){
            return null;
        }else if(r.objeto == object){
            return r;
        }else if(r.objeto < object){
            return search(object,r.derecha);
        }else{
            return search(object,r.izquierda);
        }
    }
    
    public int getFe(Node r){
        if (r== null){
            return -1;
        }else{
            return r.fe;
        }
    }
    
    public Node rotacionIzquierda(Node r){
        Node aux = r.izquierda;
        r.izquierda = aux.derecha;
        aux.derecha=r;
        r.fe=Math.max(getFe(r.izquierda), getFe(r.derecha))+1;
        aux.fe=Math.max(getFe(aux.izquierda), getFe(aux.derecha))+1;
        return aux;
    }
    
    public Node rotacionDerecha(Node r){
        Node aux = r.derecha;
        r.derecha = aux.izquierda;
        aux.izquierda=r;
        r.fe=Math.max(getFe(r.izquierda), getFe(r.derecha))+1;
        aux.fe=Math.max(getFe(aux.izquierda), getFe(aux.derecha))+1;
        return aux;
    }
    
    public Node rotacionDobleIzquierda(Node r){
        Node temp;
        r.izquierda = rotacionDerecha(r.izquierda);
        temp = rotacionIzquierda(r);
        return temp;
    }
    
    public Node rotacionDobleDerecha(Node r){
        Node temp;
        r.derecha = rotacionIzquierda(r.derecha);
        temp = rotacionDerecha(r);
        return temp;
    }
    
    public Node insertAVL(Node nuevo, Node subarbol){
        Node nuevaraiz = subarbol;
        if(nuevo.objeto<subarbol.objeto){
            if(subarbol.izquierda == null){
                subarbol.izquierda=nuevo;
            }else{
                subarbol.izquierda=insertAVL(nuevo,subarbol.izquierda);
                if((getFe(subarbol.izquierda)-getFe(subarbol.derecha))==2){
                    if(nuevo.objeto<subarbol.izquierda.objeto){
                        nuevaraiz=rotacionIzquierda(subarbol);
                    }else{
                        nuevaraiz=rotacionDobleIzquierda(subarbol);
                    }
                }
            }
        }else if(nuevo.objeto>subarbol.objeto){
            if(subarbol.derecha==null){
                subarbol.derecha=nuevo;
            }else{
                subarbol.derecha=insertAVL(nuevo,subarbol.derecha);
                if((getFe(subarbol.derecha)-getFe(subarbol.izquierda))==2){
                    if(nuevo.objeto>subarbol.derecha.objeto){
                        nuevaraiz=rotacionDerecha(subarbol);
                    }else{
                        nuevaraiz=rotacionDobleDerecha(subarbol);
                    }
                }
            }
        }else{
            System.out.println("Nodo duplcado");
        }
        if((subarbol.izquierda==null) && (subarbol.derecha!=null)){
            subarbol.fe=subarbol.derecha.fe+1;
        }else if((subarbol.derecha==null)&&(subarbol.izquierda!=null)){
            subarbol.fe=subarbol.izquierda.fe+1;
        }else{
            subarbol.fe=Math.max(getFe(subarbol.izquierda), getFe(subarbol.derecha))+1;
        }
        return nuevaraiz;
    }
    
    public void insert(int obj){
        Node nuevo=new Node(obj);
        if(raiz==null){
            raiz=nuevo;
        }else{
            raiz=insertAVL(nuevo,raiz);
        }
    }
    
    public void preOrder(Node root){
        if (root!=null){
            System.out.print(root.objeto+", ");
            preOrder(root.izquierda);
            preOrder(root.derecha);
        }
    }
    
    public void inOrder(Node root){
        if (root!=null){
            inOrder(root.izquierda);
            System.out.print(root.objeto+", ");
            inOrder(root.derecha);
        }
    }
    
    public void posOrder(Node root){
        if (root!=null){
            posOrder(root.izquierda);
            posOrder(root.derecha);
            System.out.print(root.objeto +", ");
        }
    }
}
