from edu.circudoublistnode import CircuDoubListNode
from edu.CircuDoubleList import CircuDoubleList

if __name__ == '__main__':

    dNueva = CircuDoubleList()
    print(dNueva.isEmpty())
    print(dNueva.getSize())
    dNueva.add("o1")
    dNueva.add("o2")
    dNueva.add("o3")
    dNueva.insertHead("o0")

    print(dNueva.Show())
    print(dNueva.Show_Backwards())

    print("remove")
    dNueva.remove("o0")

    print(dNueva.Show())
    print(dNueva.Show_Backwards())

"""    
public boolean isEmpty(); readycd

public int getSize(); readycd

public void clear(); readycd

public Object getHead(); readycd 

public Object getTail(); readycd

public ListNode search(Object object); readycd

public boolean add(Object object); readycd

public boolean insert(ListNode node, Object object); 

public boolean insert(Object ob, Object object); 

public boolean insertHead(Object ob, Object object); readycd

public boolean insertTail(Object ob, Object object); readycd

public boolean remove(ListNode node); readycd 

public boolean remove(Object object); readycd 

public boolean contains(Object object); readycd 

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
