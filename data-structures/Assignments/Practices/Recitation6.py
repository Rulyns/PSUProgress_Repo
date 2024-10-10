class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class LinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out)

    __repr__=__str__

    def isEmpty(self):
        return self.head==None


    def __len__(self):
        current=self.head
        count=0
        while current is not None:
            count += 1
            current = current.next    
        return count


    def add(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    

    def duplicate(self, item):
        # YOUR CODE STARTS HERE
        current = self.head
        while current is not None:
            if item == current.value:
                dupNode = Node(item)
                if current == self.head: # if item is in beginning on link list
                    dupNode.next = self.head
                    self.head = dupNode
                elif current == self.tail: # if item is in end of link list
                    current.next = dupNode
                else: # if item is in between
                    if previous.value != dupNode.value:
                        previous.next = dupNode
                        dupNode.next = current
            previous = current
            current = current.next
        self.tail = previous # this should run once the loop is at it's last node
        pass
