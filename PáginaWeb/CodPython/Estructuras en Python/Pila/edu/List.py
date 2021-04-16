from edu.ListNode import ListNode

import numpy as np

class ListNode:

    def __init__(self, object=None, next=None):
        self.object = object
        self.next = next

    def is_equals(self, object):
        if self.object.str() == object.str():
            return True
        else:
            return False

    def __eq__(self, ListNode):
        if self.object == ListNode:
            return True
        else:
            return False

    def __str__(self):
        return str("ListNode{") + str("object=") + str(self.object) + str(", next=") + str(self.next) + str("}")

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

    def insertn(self, node, object):
        try:
            if node.next == None:
                self.add(object)
            else:
                newNode = ListNode(object)
                newNode.next = node.next
                node.next = newNode
                self.size += 1
            return True
        except:
            print("Exception")
            return False

    def insert(self, ob, object):
        try:
            if ob != None:
                node = self.search(ob)
                if node != None:
                    return self.insertn(node, object)
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

    def __contains__(self, object):
        self.inode = self.head
        while self.inode != None:
            if self.inode.object == object:
                return True
            self.inode = self.inode.next
        return False

    def toarray(self):
        if self.getSize() > 0:
            arredo = []
            self.inode = self.head
            for i in range(self.getSize()):
                arredo.append(self.inode)
                self.inode = self.inode.next
            return arredo
        else:
            return -1

    def to_array(self, object):
        if self.getSize() > 0:
            object = np.zeros(self.getSize())
            self.inode = self.head
            object[0] = self.head.object
            for i in range(1, self.getSize()):
                self.inode = self.inode.next
                object[i] = self.inode.object
            return object
        return -1

    def sublist(self, desde, hasta):
        try:
            if self.getSize() > 0:
                if desde != None and hasta != None:
                    listed = List()
                    self.inode = self.head
                    while self.inode.next != None:
                        self.inode = self.inode.next
                        if self.inode == desde:
                            listed.add(self.inode)
                            while self.inode != hasta:
                                self.inode = self.inode.next
                                listed.add(self.inode)
                            break
                    return listed
                else:
                    return "From or to invalid"
            else:
                return -1
        except:
            print("Exception")
            return False

    def sortlist(self):
        if self.getSize() > 0:
            arreglo = np.zeros(self.getSize())
            self.inode = self.head
            for i in range(self.getSize()):
                arreglo[i] = self.inode.object
                self.inode = self.inode.next

            list = sorted(arreglo)
            self.clear()
            for elem in list:
                self.add(elem)
            return self
        else:
            -1

    def __str__(self):
        return str("List{") + str("head=") + str(self.head) + str(", tail=") + str(self.tail) + str(", size=") + str(
            self.size) + str("}")

    def Show(self):
        impresion = "["
        inode = self.head
        while inode != None:
            impresion += str(inode.object) + ","
            inode = inode.next
        impresion += "]"
        return impresion





