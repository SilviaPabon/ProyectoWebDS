
class DoubleListNode:

    #constructor
    def __init__(self, object=None, next=None, previous=None):
        self.object = object
        self.next = next
        self.previous = previous
        
    def is_equals(self, object):
        if self.object.str() == object.str():
            return True
        else:
            return False

    def __eq__(self, do_listnode):
        if self.object == do_listnode:
            return True
        else:
            return False

    def __str__(self):
        return str("ListNode{") + str("object=") + str(self.object) + str(", next=") + str(self.next) + str("}")
