'''
General Notes

"nextval" actually means the next node in the linked list
"dataval" means the value associated within the node
'''

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def addAtBeginning(self, newdata):
        new_node = Node(newdata)
        new_node.nextval = self.headval
        self.headval = new_node
    def addAtEnd(self, newdata):
        current_node = self.headval
        new_node = Node(newdata)
        # Check edge case if head is null
        if current_node is None:
            current_node = new_node
        while current_node.nextval:
            current_node = current_node.nextval
        current_node.nextval=new_node

    def addBetweenNodes(self, left_node_from_target, newdata):
        new_node = Node(newdata)
        # Check edge case for left_node_from_target is empty
        new_node.nextval = left_node_from_target.nextval
        left_node_from_target.nextval = new_node

    def deleteNode(self, target_node_val):
        current_node = self.headval

        if current_node is not None:
            if current_node.dataval == target_node_val:
                self.head = target_node_val
                current_node = None
                return
                
        while current_node.nextval:
            if current_node.dataval == target_node_val:
                break
            prev = current_node
            current_node = current_node.nextval

        if current_node == None:
            return

        # Setting the linkedlist so that the previous node is linked to the
        # node right to the target node. Then setting the current node to none to delete it safely.
        prev.nextval = current_node.nextval
        current_node = None



list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

# Link first node to second node
list1.headval.nextval = e2
# Link second node to third node
e2.nextval = e3

list1.addAtEnd("JasonKim")
list1.listprint()
