
class CircuListNode:

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
        return str("ListNode{") + str("object=") + str(self.object) + str("}")
