/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Daniel
 */
public class Node {
    public Node izquierda,derecha;
    public int objeto, fe;
    
    public Node(int object){
        this.izquierda = null;
        this.derecha = null;
        this.objeto = object;
        this.fe = 0;
    }
}
