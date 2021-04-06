from edu.circudoublistnode import CircuDoubListNode
from edu.CircuDoubleList import CircuDoubleList

if __name__ == '__main__':

    dNueva = CircuDoubleList()
    print(dNueva.isEmpty())
    print(dNueva.getSize())
    dNueva.add("o1")
    dNueva.add("o2")
    dNueva.add("o3")


"""    
public boolean isEmpty(); 

public int getSize(); 

public void clear(); 

public Object getHead(); 

public Object getTail(); 

public ListNode search(Object object); 

public boolean add(Object object); 

public boolean insert(ListNode node, Object object); 

public boolean insert(Object ob, Object object); 

public boolean insertHead(Object ob, Object object); 

public boolean insertTail(Object ob, Object object); 

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
