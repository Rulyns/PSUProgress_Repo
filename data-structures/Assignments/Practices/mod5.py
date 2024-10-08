class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

    def __str__(self):
        return f"Node({self.value})"

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
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

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


    def __contains__(self,value):
        current=self.head
        while current is not None:
            if current.value==value:
                return True
            else:
                current=current.next
        return False


    def __delitem__(self,position):   
        if self.isEmpty():
            print('List is empty')
            return None
        if len(self)>=position:
            current=self.head
            previous=None
            count=1
            while count<position:
                    previous=current
                    current=current.next
                    count+=1
            if previous is None:
                self.head=current.next
                current.next=None
            elif current.next is None:
                previous.next=None
                self.tail=previous
            else:
                previous.next=current.next
                current.next=None