import io
#para realizar los nodos
import networkx as nx
#para graficar
import matplotlib.pyplot as plt
#para obtener abstract syntax tree
import ast

code = """
class List:

    def __init__(self):
        self.clear()

    def clear(self):
        self.head = None
        self.tail = None
        self.inode = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def getSize(self):
        return self.size

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def search(self, object):
        self.inode = self.head
        while self.inode != None:
            if self.inode.object == object:
                return self.inode
            self.inode = self.inode.next
        return None

    # add o append?
    def add(self, object):
        return self.instertTail(object)

    def instertTail(self, object):
        try:
            self.inode = ListNode(object)
            if self.getSize() == 0:
                self.head = self.inode
                self.tail = self.head
            else:
                self.tail.next = self.inode
                self.tail = self.tail.next
            self.size += 1
            return True
        except:
            print("Exception")
            return False


    def insertHead(self, object):
        try:
            self.inode = ListNode(object)
            if self.getSize() == 0:
                self.head = self.inode
                self.tail = self.head
            else:
                self.head = ListNode(object, self.head)
            self.size += 1
            return True
        except:
            print("Exception")
            return False

    def insertn(self, nodo, object):
        try:
            if nodo.next == None:
                self.add(object)
            else:
                newNode = ListNode(object)
                newNode.next = nodo.next
                nodo.next = newNode
                self.size += 1
            return True
        except:
            print("Exception")
            return False

    def insert(self, ob, object):
        try:
            if ob != None:
                nodo = self.search(ob)
                if nodo != None:
                    return self.insertn(nodo, object)
                else:
                    return False
            else:
                return False
        except:
            print("Exception")
            return False

    def remove(self, ListNode):
        if self.getSize() > 0:
            if self.head == self.tail and self.head == ListNode:
                self.clear()
                --self.getSize()
                return True
            elif ListNode == self.head:
                self.head = self.head.next
                --self.getSize()
                return True
            else:
                prev = self.head
                self.inode = self.head.next
                while self.inode != None and self.inode != ListNode:
                    prev = prev.next
                    self.inode = self.inode.next
                if self.inode != None:
                    prev.next = self.inode.next
                    if self.inode == self.tail:
                        self.tail = prev
                --self.getSize()
                return True
            return True
        else:
            return False

    def remove(self, object):
        if self.getSize() > 0:
            if self.head == self.tail and self.head == object:
                self.clear()
                self.size -= 1
                return True
            elif object == self.head.object:
                self.head = self.head.next
                self.size -= 1
                return True
            else:
                prev = self.head
                self.inode = self.head.next
                while self.inode != None and self.inode.object != object:
                    prev = prev.next
                    self.inode = self.inode.next
                if self.inode != None:
                    prev.next = self.inode.next
                    if self.inode == self.tail:
                        self.tail = prev
                    self.size -= 1
                return True
            return True
        else:
            return False
"""
code_ast = ast.parse(code)

g = nx.Graph()
list = []
listaatributos = []
dict = {}
f = ""
for nodo in ast.walk(code_ast):
    if isinstance(nodo, ast.Module):
        for i in nodo.body:
            clase = i.name

    if isinstance(nodo, ast.ClassDef):
        for e in nodo.body:
            print("nombre " + e.name)
            g.add_node(e.name)
            list.append(e)
            if isinstance(e, ast.FunctionDef):
                for nodes in ast.walk(e):
                    if isinstance(nodes, ast.arg):
                        if nodes.arg == 'self':
                            pass
                        else:
                            print(nodes.arg)
                            dict.setdefault(e.name, [])
                            dict[e.name].append(nodes.arg)
                            stringg = str(nodes.arg)
                            g.add_node(stringg)
                    if isinstance(nodes, ast.Attribute):
                        if e.name == 'clear':
                            print("atributo", nodes.attr)
                            g.add_node(nodes.attr)
                            listaatributos.append(nodes)

for elem in list:
    g.add_edge(clase, elem.name)
    if elem.name in dict:
        print("prueba", elem.name)
        for each in dict[elem.name]:
            agregar = str(each)
            g.add_edge(elem.name, agregar)

for elem2 in listaatributos:
    g.add_edge(clase, elem2.attr)

pos = nx.spring_layout(g, scale= 2, seed=109)
plt.figure(figsize=(15, 12))
nx.draw_networkx_nodes(g, pos=pos, node_color='green')
nx.draw_networkx(g, pos=pos, nodelist=["List"], node_color='#A0CBE2', font_size=10)
nx.draw_networkx(g, pos=pos, nodelist=["object", "ob", "ListNode", "nodo"], node_color='#a0e2d8', font_size=10)
nx.draw_networkx(g, pos=pos, nodelist=["head", "tail", "inode", "size"], node_color='#e2a0cb', font_size=10)
plt.savefig("filename1.jpg")

