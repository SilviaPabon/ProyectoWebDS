

public class Node {
    public Node izquierda;
    public Node derecha;
    public int objeto;
    
    public Node(int object){
        this.izquierda = null;
        this.derecha = null;
        this.objeto = object;
    }
    
    public Node (Node left, int object, Node right){
        this.izquierda = left;
        this.derecha = right;
        this.objeto = object;
    }
    
    @Override
    public String toString(){
        return "Node{" +
                "left="+izquierda+
                ", right="+derecha+
                ", object="+objeto+
                '}';
    }
}
