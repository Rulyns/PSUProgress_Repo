# Queue implementation using a Python List
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value): # Simplified version of insert using a helper method
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:      # This will allow repeated values to be placed in the tree. To avoid this, we do: elif(value>node.value):
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def bfs(self):
        if self.root is None:
            return 'Tree is Empty'

        q=Queue()
        visited=[]
        q.enqueue(self.root)

        while not q.isEmpty():
            node=q.dequeue()
            visited.append(node.value)

            #Left
            if node.left is not None:
                q.enqueue(node.left)

            #Right
            if node.right is not None:
                q.enqueue(node.right)

        return visited

    def preorder(self, node): # traversal by left side
        if node is not None:
            print(node.value, end=' ') # Head first
            self.preorder(node.left) # left second
            self.preorder(node.right) # right third

    def inorder(self, node): # traversal by bottom side
        if node is not None:
            self.inorder(node.left) # Left first
            print(node.value, end=' ') # Head Second
            self.inorder(node.right) # right third

    def postorder(self, node): # traveral by right side
        if node is not None:
            self.postorder(node.left) # left first
            self.postorder(node.right) # right second
            print(node.value, end=' ') # head last