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
        pass

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

    def remove(self, ListNode):
        pass

    def remove(self, object):
        pass

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





