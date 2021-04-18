from edu.List import List
from edu.ListNode import ListNode

if __name__=='__main__':
    nueva = List()
    print("Probar, vacío y agregar")
    print(nueva.isEmpty())
    print(nueva.add(1))
    nueva.add(2)
    nueva.add(3)
    nueva.add(3.1)
    nueva.add(4)

    print("Imprimir lista, probar vacío, obtener cola")
    print(nueva)
    print(nueva.isEmpty())
    print(nueva.getTail().object)

    print("Insertar cabeza en llena, vacía y vacía")
    nueva.insertHead("Inicio")
    print(nueva.Show())
    nueva2 = List()
    nueva2.insertHead("Inicio2")
    print(nueva2.Show())
    nueva2.insertHead("o2")
    print(nueva2.Show())

    print("Eliminar")
    nueva.remove("Inicio")
    print(nueva.Show())
    print(nueva.getSize())

    print("Buscar/contains")
    nueva.search("Inicio")
    print(nueva2.search("I"))
    print(nueva2)
    print(nueva2.__contains__("o2"))
    print("arreglo")
    for obj in nueva.toarray():
        print(obj)
    print("arreglo")


    nueva.insert(4, 33)
    print(nueva)



"""    
public boolean isEmpty(); //ready

public int getSize(); //ready

public void clear(); //ready

public Object getHead(); //ready

public Object getTail(); //ready

public ListNode search(Object object); //ready

public boolean add(Object object); //ready

public boolean insert(ListNode node, Object object); //ready

public boolean insert(Object ob, Object object); //ready

public boolean insertHead(Object ob, Object object); //ready

public boolean insertTail(Object ob, Object object); //ready

public boolean remove(ListNode node); //ready

public boolean remove(Object object); //ready
//expension
public boolean contains(Object object); //ready

public Object[] toArray(); //ready

public Object[] toArray(Object[] object); //ready

public Object getBeforeTo();

public ListNode getBeforeTo(ListNode node);

public Object getNextTo();

public Object getNextTo(ListNode node);

public List subList(ListNode from, ListNode to); //ready

public List sortList(); //ready
"""




