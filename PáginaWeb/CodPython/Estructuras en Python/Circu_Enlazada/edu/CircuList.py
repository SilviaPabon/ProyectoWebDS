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
        a = iter(self)
        while next(a, None):
            if (next(a, None).equals(object).toString):
                return next(a, None)
        return None

    # add o append?
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
            self.size += 1
            return True
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

    def __str__(self):
        return str("List{") + str("head=") + str(self.head) + str(", tail=") + str(self.tail) + str(", size=") + str(
            self.size) + str("}")

    def Show(self):
        if self.isEmpty() == True:
            print("-1")
        resultado = ""
        self.inode = self.head
        while self.inode != self.tail:
            resultado += str(self.inode.object) + "->"
            self.inode = self.inode.next
        resultado += str(self.tail.object) + "->" + str(self.head.object)
        return resultado






