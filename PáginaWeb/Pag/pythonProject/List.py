import numpy as np

class List:

    def __init__(self):
        self.head = None
        self.tail = None
        self.inode = None
        self.size = 0

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
            #self.inode = ListNode(object)
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
            #self.inode = ListNode(object)
            if self.getSize() == 0:
                self.head = self.inode
                self.tail = self.head
            #else:
                #self.head = ListNode(object, self.head)
            self.size += 1
            return True
        except:
            print("Exception")
            return False

    def insertn(self, node, object):
        try:
            if node.next == None:
                self.add(object)
            """else:
                newNode = ListNode(object)
                newNode.next = node.next
                node.next = newNode
                self.size += 1"""
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
            if self.head == self.tail and self.head == node:
                self.clear()
                --self.getSize()
                return True
            elif node == self.head:
                self.head = self.head.next
                --self.getSize()
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






