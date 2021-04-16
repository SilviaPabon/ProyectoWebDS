
public class BinTree {
    public Node root;
    
    public BinTree(){
        this.root = null;
    }
    
    public boolean isEmpty(){
        return root == null;
    }
    
    public String preOrder(Node root){
        String obj = "";
        if (root!=null){
            System.out.print(root.objeto+"-");
            preOrder(root.izquierda);
            preOrder(root.derecha);
        }
        return obj;
    }
    
    public String inOrder(Node root){
        String obj = "";
        if (root!=null){
            inOrder(root.izquierda);
            System.out.print(root.objeto+"-");
            inOrder(root.derecha);
        }
        return obj;
    }
    
    public String posOrder(Node root){
        String obj = "";
        if (root!=null){
            posOrder(root.izquierda);
            posOrder(root.derecha);
            System.out.print(root.objeto +"-");
        }
        return obj;
    }
    
    public void insert(int obj){
        Node nuevo= new Node(obj);
        if(root == null){
            root = nuevo;
        }else{
            Node aux = root;
            Node padre;
            while(true){
                padre = aux;
                if (obj < aux.objeto){
                    aux = aux.izquierda;
                    if (aux == null){
                        padre.izquierda=nuevo;
                        return;
                    }
                }else{
                    aux = aux.derecha;
                    if (aux == null){
                        padre.derecha=nuevo;
                        return;
                    }
                }
            }
        }
    }
    
    public boolean search(int obj){
        Node aux = root;
        while(aux.objeto!=obj){
            if (obj<aux.objeto){
                aux = aux.izquierda;
            }else{
                aux = aux.derecha;
            }
            if (aux == null){
                return false;
            }
        }
        return true;
    }

    public boolean remove(int obj){
        Node aux = root;
        Node padre = root;
        boolean izq = true;
        while(aux.objeto != obj){
            padre = aux;
            if (obj<aux.objeto){
                izq = true;
                aux = aux.izquierda;
            }else{
                izq = false;
                aux = aux.derecha;
            }
            if ( aux == null){
                return false;
            }
        }
        if (aux.izquierda == null && aux.derecha == null){ //Nodo hoja
            if (aux == root){
                root = null;
            }else if (izq){
                padre.izquierda = null;
            }else{
                padre.derecha = null;
            }
        }else if(aux.derecha==null){
            if (aux == root){
                root = aux.izquierda;
            }else if (izq){
                padre.izquierda = aux.izquierda;
            }else{
                padre.derecha = aux.izquierda;
            }
        }else if(aux.izquierda == null){
            if (aux == root){
                root = aux.derecha;
            }else if (izq){
                padre.izquierda = aux.derecha;
            }else{
                padre.derecha = aux.derecha;
            }
        }else{
            Node reemplazo = obtenerNodoReemplazo(aux);
            if(aux == root){
                root = reemplazo;
            }else if(izq){
                padre.izquierda=reemplazo;
            }else{
                padre.derecha = reemplazo;
            }
            reemplazo.izquierda = aux.izquierda;
        }
    return true;
    }
    public Node obtenerNodoReemplazo(Node NodoR){
        
        Node reemplazopadre = NodoR;
        Node reemplazo = NodoR;
        Node aux = NodoR.derecha;
        while(aux != null){
            reemplazopadre = reemplazo;
            reemplazo = aux;
            aux = aux.izquierda;
        }
        if (reemplazo != NodoR.derecha){
            reemplazopadre.izquierda = reemplazo.derecha;
            reemplazo.derecha = NodoR.derecha;
        }
        return reemplazo;
    }
    
}
/*
    
//Raíz
if(root.objeto instanceof Node){
    obj = ((Node) root.objeto).objeto.toString();
}else{
    obj=root.objeto.toString();
}
//Izquierda
if (root.izquierda !=null){
    obj = obj + preOrder(root.izquierda);
}else{
    obj = obj + "";
}
//Derecha
if(root.derecha !=null){
    obj = obj+preOrder(root.derecha);
}else{
    obj = obj+"";
}

obj = (root.objeto instanceof Node) ? ((Node) root.objeto).objeto.toString(): root.objeto.toString(); //Raiz
obj = obj + ((root.izquierda !=null) ? preOrder(root.izquierda):""); //Izquierda
obj = obj + ((root.derecha !=null) ? preOrder(root.derecha):""); //Derecha
*/