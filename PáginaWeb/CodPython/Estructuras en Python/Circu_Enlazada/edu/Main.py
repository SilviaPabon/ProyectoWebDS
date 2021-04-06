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
    print(nueva.Show())

    nueva2 = CircuList()
    print(nueva2.getTail())







"""    
public boolean isEmpty(); //readyc

public int getSize(); //readyc

public void clear(); //readyc

public Object getHead(); //readyc

public Object getTail(); //readyc

public ListNode search(Object object); 

public boolean add(Object object); //readyc

public boolean insert(ListNode node, Object object); 

public boolean insert(Object ob, Object object); 

public boolean insertHead(Object ob, Object object); 

public boolean insertTail(Object ob, Object object); //readyc

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




