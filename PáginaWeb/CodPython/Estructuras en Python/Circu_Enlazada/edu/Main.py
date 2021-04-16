from edu.CircuList import CircuList
from edu.CircuListNode import CircuListNode

if __name__=='__main__':
    nueva = CircuList()
    print("Probar, vacío y agregar")
    print(nueva.isEmpty())
    print(nueva.add(1))
    nueva.add(2)
    nueva.add(3)

    print("Imprimir lista, probar vacío, obtener cola")
    print(nueva.isEmpty())
    print(nueva.getTail())
    print(nueva.show())

    nueva2 = CircuList()
    print(nueva2.getTail())

    print("Buscar")
    print(nueva.search(4))
    nueva.instertHead("inicio")
    print(nueva.show())

    nueva2.instertHead(1)
    nueva2.add(2)
    nueva2.add(3)
    nueva2.add(4)
    nueva2.insert(4, "k")
    print(nueva2.show())
    print(nueva2.__contains__("k"))

    nueva2.removen("k")
    print(nueva2.show())









"""    
public boolean isEmpty(); //readyc

public int getSize(); //readyc

public void clear(); //readyc

public Object getHead(); //readyc

public Object getTail(); //readyc

public ListNode search(Object object); //readyc

public boolean add(Object object); //readyc

public boolean insert(ListNode node, Object object); //readyc

public boolean insert(Object ob, Object object); //readyc

public boolean insertHead(Object ob, Object object); //readyc

public boolean insertTail(Object ob, Object object); //readyc

public boolean remove(ListNode node); //readyc

public boolean remove(Object object); //readyc

public boolean contains(Object object); //readyc

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




