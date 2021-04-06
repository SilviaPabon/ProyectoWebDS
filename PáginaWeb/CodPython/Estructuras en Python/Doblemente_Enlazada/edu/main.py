from edu.doublelistnode import DoubleListNode
from edu.DoubleList import DoubleList

if __name__ == '__main__':

    dNueva = DoubleList()
    print(dNueva.isEmpty())
    print(dNueva.getSize())
    dNueva.add("o1")
    dNueva.add("o2")
    dNueva.add("o3")
    print(dNueva.isEmpty())
    print(dNueva.getSize())
    print(dNueva.isEmpty())
    print(dNueva.instertHead("o0"))
    print(dNueva.getTail().object)
    print(dNueva.Show())
    print(dNueva.Show_Backwards())
    print(dNueva.getSize())


"""    
public boolean isEmpty(); //readyd

public int getSize(); //readyd

public void clear(); //readyd

public Object getHead(); //readyd

public Object getTail(); //readyd

public ListNode search(Object object); 

public boolean add(Object object); //readyd

public boolean insert(ListNode node, Object object); 

public boolean insert(Object ob, Object object); 

public boolean insertHead(Object ob, Object object); //ready

public boolean insertTail(Object ob, Object object); //readyd

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
