from edu.List import List
from edu.ListNode import ListNode

class liststack(List):

    def __init__(self):
        self.d = List()
        self.top = None
        self.size = 0

    def clear(self):
        while self.isEmpty() == False:
            tmp = self.top
            self.top = self.top.next
            tmp.next = None
        self.size = 0

    def isEmpty(self):
        return self.top == None

    def getSize(self):
        return self.size

    def peek(self):
        try:
            if self.getSize() == 0:
                return -1
            else:
                self.inode = self.top.object
                return self.inode
        except:
            print("Exception")
            return False

    def pop(self):
        try:
            if self.getSize() == 0:
                return -1
            else:
                self.inode = self.top.object
                self.top = self.top.next
                self.size -= 1
                return self.inode
        except:
            print("Exception")
            return False

    def push(self, object):
        try:
            nodopila = ListNode(object)
            if self.size == 0:
                nodopila.next = None
                self.top = nodopila
            else:
                nodopila.next = self.top
                self.top = nodopila
            print(object)
            self.size -= 1
            return True
        except:
            print("Exception")
            return False

    def search(self, object):
        super().search(object)
        return True

    def searchs(self, object):
        try:
            if self.size == 0:
                return False
            else:
                inode = self.top.object
                tmp = self.top.next
                while inode != object and tmp != None:
                    inode = tmp.next.object
                return True
        except:
            print("Exception")
            return False