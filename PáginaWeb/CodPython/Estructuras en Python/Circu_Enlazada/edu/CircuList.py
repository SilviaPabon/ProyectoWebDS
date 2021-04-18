from edu.CircuListNode import CircuListNode

class CircuList:

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
        if self.isEmpty() == True:
            print("-1")
            return False
        else:
            self.inode = self.head
            return self.inode.object

    def getTail(self):
        if self.isEmpty() == True:
            print("-1")
            return False
        else:
            self.inode = self.head
            while self.inode != self.tail:
                self.inode = self.inode.next
            return self.tail.object

    def search(self, object):
        self.inode = self.head
        while True:
            if self.inode.object == object:
                return self.inode
            self.inode = self.inode.next
            if self.inode == self.head:
                break
        return None

    def add(self, object):
        return self.instertTail(object)

    def instertTail(self, object):
        try:
            self.inode = CircuListNode(object)
            if self.isEmpty() == True:
                self.head = self.inode
                self.tail = self.head
            else:
                self.tail.next = self.inode
                self.tail = self.inode
            self.tail.next = self.head
            self.size += 1
            return True
        except:
            print("Exception")
            return False


    def instertHead(self, object):
        try:
            self.inode = CircuListNode(object)
            if self.getSize() == 0:
                self.head = self.inode
                self.tail = self.head
            else:
                self.head = CircuListNode(object, self.head)
            self.tail.next = self.head
            self.size += 1
            return True
        except:
            print("Exception")
            return False

    def insertn(self, node, object):
        try:
            if node.next == None:
                self.add(object)
            elif node.next == self.head:
                self.add(object)
            else:
                newNode = CircuListNode(object)
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


    def removen(self, node):
        if self.getSize() > 0:
            if node != None:
                if self.head == self.tail and self.head == node:
                    self.clear()
                    self.size -= 1
                    return True
                elif node == self.head:
                    self.head = self.head.next
                    self.size -= 1
                    return True
                else:
                    prev = self.head
                    self.inode = self.head.next
                    while self.inode != None and self.inode != node:
                        prev = prev.next
                        self.inode = self.inode.next
                    if self.inode != None:
                        prev.next = self.inode.next
                        if self.inode == self.tail:
                            self.tail = prev
                    self.size -= 1
                    return True
            else:
                return False
        else:
            return False

    def remove(self, object):
        if self.getSize() > 0:
            if object != None:
                node = self.search(object)
                if node != None:
                    return self.removen(node)
                else:
                    return False
            else:
                return False
        else:
            return False

    def __contains__(self, object):
        self.inode = self.head
        while True:
            if self.inode.object == object:
                return True
            self.inode = self.inode.next
            if self.inode == self.head:
                break
        return False

    def __str__(self):
        return str("List{") + str("head=") + str(self.head) + str(", tail=") + str(self.tail) + str(", size=") + str(
            self.size) + str("}")

    def show(self):
        if self.isEmpty() == True:
            print("-1")
        resultado = ""
        self.inode = self.head
        while self.inode != self.tail:
            resultado += str(self.inode.object) + "->"
            self.inode = self.inode.next
        resultado += str(self.tail.object) + "->" + str(self.head.object)
        return resultado






