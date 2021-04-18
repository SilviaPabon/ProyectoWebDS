from edu.circudoublistnode import CircuDoubListNode

class CircuDoubleList:

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
        if self.getSize() == 0:
            print("-1")
            return False
        else:
            return self.head.previous

    def search(self, object):
        self.inode = self.head
        while True:
            if self.inode.object == object:
                return self.inode
            self.inode = self.inode.next
            if self.inode == self.head:
                break
        return None

    # add o append?
    def add(self, object):
        return self.instertTail(object)

    def instertTail(self, object):
        try:
            self.inode = CircuDoubListNode(object, None, None)
            if self.getSize() == 0:
                self.inode.previous = self.inode
                self.inode.next = self.inode
                self.head = self.inode
            else:
                ult = self.head.previous
                self.inode.next = self.head
                self.inode.previous = ult
                self.head.previous = self.inode
                ult.next = self.inode
            self.size += 1
            return True
        except:
            print("Exception")
            return False

    def insertHead(self, object):
        try:
            inode = CircuDoubListNode(object)
            if self.isEmpty() == True:
                inode.previous = inode
                inode.next = inode
                self.head = inode
            else:
                ult = self.head.previous
                inode.previous = ult
                ult.next = inode
                self.head.previous = inode
                inode.next = self.head
                self.head = inode
            self.size += 1
            return True
        except:
            print("Exception")
            return False

    def removen(self, node):
        if self.getSize() > 0:
            nodeDL = self.search(node.object)
            if nodeDL != None:
                if self.head == nodeDL:
                    self.head = nodeDL.next
                if nodeDL.next != None:
                    nodeDL.next.previous = nodeDL.previous
                if nodeDL.previous != None:
                    nodeDL.previous.next = nodeDL.next
                self.size -= 1
                return True
            else:
                return -1
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
        return str("DoubleList{") + str("head=") + str(self.head) + str(", tail=") + str(self.tail) + str(", size=") + str(
            self.size) + str("}")

    def Show(self):
        resultado = ""
        self.inode = self.head
        if self.isEmpty() == True:
            print("-1")
        else:
            resultado += str(self.head.object) + " <--> "
            self.inode = self.head.next
            while True:
                resultado += str(self.inode.object) + " <--> "
                self.inode = self.inode.next
                if self.inode.next == self.head:
                    break
            resultado += str(self.inode.object) + " <--> "
            self.inode = self.inode.next
            resultado += "inicio " + str(self.inode.object) + "\n"
        return resultado

    def Show_Backwards(self):
        resultado = ""
        self.inode = self.head.previous
        if self.isEmpty() == True:
            print("-1")
        elif (self.head.previous == self.head):
            resultado += str(self.head.object) + " <--> " + str(self.inode.object) + "\n"
        else:
            self.inode = self.head.previous
            while True:
                resultado += str(self.inode.object) + " <--> "
                self.inode = self.inode.previous
                if self.inode.previous == self.head.previous:
                    break
            resultado += str(self.inode.object) + " <--> "
            self.inode = self.inode.previous
            resultado += "inicio " + str(self.inode.object) + "\n"
        return resultado





