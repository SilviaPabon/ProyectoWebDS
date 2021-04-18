from edu.doublelistnode import DoubleListNode

class DoubleList:

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
            self.inode = DoubleListNode(object, None, None)
            if self.getSize() == 0:
                self.tail = self.inode
                self.head = self.tail
            else:
                self.tail.next = self.inode
                self.inode.previous = self.tail
                self.tail = self.inode
                self.tail.next = None
            self.size += 1
            return True
        except:
            print("Exception")
            return False

    def instertHead(self, object):
        try:
            self.inode = DoubleListNode(object)
            if self.getSize() == 0:
                self.head = self.inode
            else:
                self.inode.next = self.head
                self.head.previous = self.inode
                self.head = self.inode
            self.size += 1
            return True
        except:
            print("Exception")
            return False

    def insertn(self, node, object):
        try:
            if node != None:
                if node.next == None:
                    self.add(object)
                else:
                    newNode = DoubleListNode(object)
                    newNode.next = node.next
                    node.next = newNode
                    newNode.previous = node
                    if newNode.next != None:
                        newNode.next.previous = newNode
                    self.size += 1
                return True
            else:
                return False
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
        while self.inode != None:
            if self.inode.object == object:
                return True
            self.inode = self.inode.next
        return False

    def __str__(self):
        return str("DoubleList{") + str("head=") + str(self.head) + str(", tail=") + str(self.tail) + str(", size=") + str(
            self.size) + str("}")

    def Show(self):
        impresion = "["
        inode = self.head
        while inode != None:
            impresion += str(inode.object) + ","
            inode = inode.next
        impresion += "]"
        return impresion

    def Show_Backwards(self):
        impresion = "["
        inode = self.tail
        while inode != None:
            impresion += str(inode.object) + ","
            inode = inode.previous
        impresion += "]"
        return impresion





