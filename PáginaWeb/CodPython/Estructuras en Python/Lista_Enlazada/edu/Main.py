from edu.List import List
from edu.ListNode import ListNode

if __name__=='__main__':
    nueva = List()
    print("Probar, vacío y agregar")
    print(nueva.isEmpty())
    print(nueva.add(1))
    nueva.add(2)
    nueva.add(3)

    print("Imprimir lista, probar vacío, obtener cola")
    print(nueva)
    print(nueva.isEmpty())
    print(nueva.getTail().object)

    print("Insertar cabeza en llena, vacía y vacía")
    nueva.instertHead("Inicio")
    print(nueva.Show())
    nueva2 = List()
    nueva2.instertHead("Inicio2")
    print(nueva2.Show())
    nueva2.instertHead("o2")
    print(nueva2.Show())

    print("Eliminar")
    nueva.remove("Inicio")
    print(nueva.Show())
    print(nueva.getSize())

    print("Buscar")
    
    nueva.search("Inicio")




"""    
public boolean isEmpty(); //ready

public int getSize(); //ready

public void clear(); //ready

public Object getHead(); //ready

public Object getTail(); //ready

public ListNode search(Object object); 

public boolean add(Object object); //ready

public boolean insert(ListNode node, Object object); 

public boolean insert(Object ob, Object object); 

public boolean insertHead(Object ob, Object object); //ready

public boolean insertTail(Object ob, Object object); //ready

public boolean remove(ListNode node); 

public boolean remove(Object object);

public boolean contains(Object object); 

public Iterator<ListNode> iterator(); 

public Object[] toArray(); 

public Object[] toArray(Object[] object); 

public Object getBeforeTo();

public ListNode getBeforeTo(ListNode node);

public Object getNextTo();

public Object getNextTo(ListNode node);

public List subList(ListNode from, ListNode to);

public List sortList(); 
"""




