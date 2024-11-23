# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    """
        >>> my_tree = BinarySearchTree() 
        >>> my_tree.isEmpty()
        True
        >>> my_tree.isBalanced
        True
        >>> my_tree.insert(9) 
        >>> my_tree.getMin
        9
        >>> my_tree.insert(5) 
        >>> my_tree.insert(14)  
        >>> my_tree.insert(6)
        >>> my_tree.getMax
        14
        >>> my_tree.insert(5.5) 
        >>> my_tree.insert(7)   
        >>> my_tree.getMin
        5
        >>> my_tree.getMax
        14
        >>> 67 in my_tree
        False
        >>> 4 in my_tree
        False
        >>> 7 in my_tree
        True
        >>> 23 in my_tree
        False
        >>> 5.5 in my_tree
        True
        >>> 9 in my_tree
        True
        >>> my_tree.isEmpty()
        False
        >>> my_tree.getHeight(my_tree.root)   # Height of the tree
        3
        >>> my_tree.getHeight(my_tree.root.left.right) # 6
        1
        >>> my_tree.getHeight(my_tree.root.right) # 14
        0
        >>> my_tree.isBalanced
        False
        >>> my_tree.insert(10)
        >>> my_tree.isBalanced
        True
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
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
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.root == None
        pass


    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        # Insertion states that the leftmost root is ALWAYS our minimum root.
        location = self.root                 # start at root
        if self.isEmpty():                   # tree insertion starts balanced, and is innately balancing, so you should only check the first root node and anything to the left. You should never check right tree, 
            return None                      # since there will be no value to cause the tree to lose balance due to the special insertion and balancing helpers. Speaking of which, reminder to add balancing into insertion if needed.
        while location is not None:          # balancing will allow this to stay balanced, and therefore remove the need to check parts of the tree to the right. At least in theory.
            prev = location
            location = location.left
        return prev.value
        pass


    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE
        location = self.root #same as getMin but right side
        if self.isEmpty():                   # tree insertion starts balanced, and is innately balancing, so you should only check the first root node and anything to the left. You should never check right tree, 
            return None                      # since there will be no value to cause the tree to lose balance due to the special insertion and balancing helpers. Speaking of which, reminder to add balancing into insertion if needed.
        while location is not None:          # balancing will allow this to stay balanced, and therefore remove the need to check parts of the tree to the right. At least in theory.
            prev = location
            location = location.right
        return prev.value
        pass


    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        # Check if value is lesser or greater than whatever node is an check from there.
        ping = False
        location = self.root
        while location is not None:
            if value == location.value:
                ping = True
                return ping
            elif value > location.value:
                location = location.right
            elif value < location.value:
                location = location.left
        return ping
        pass

    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        if isinstance(node, Node) and node.value in self: # check if value is within tree being called
            if node is None:
                return 0
            else:
                # overall height is max(left_height,right_height), the max function already will tell us which one is maximum within the subtree's we just need to iterate and count.
                left_max = self.getHeight(node.left) + 1 # will recursively visit all possible nodes
                right_max = self.getHeight(node.right) + 1 # <--‘ This one as well.
                # the above will generate "sums" of different paths along the tree, in our final return, we want a "depth" that went the farthest
                return max(left_max, right_max) # Are we even allowed to use max? it was on the lab so I just followed the lectures and what I remember to the key. You can also do a small if-statement block, or do some fancy math, those always also work.
        else:
            return -1 # This negative 1, at the end of the count, subtracts the "root", since a tree counting from the roots doesnt deduce its height, it's like digging into the ground and finding out the tree is twice its size because its roots stretch so far deep.

    @property
    def isBalanced(self):  # Do not modify this method
        return self.isBalanced_helper(self.root)
    
    
    def isBalanced_helper(self, node): 
        '''
            From AVL Tree class : 
                def getBalance(self, node):
                    if node is None:
                        return 0
                    return self.getHeight(node.left) - self.getHeight(node.right)
        '''
        if node == None:
            return True
        balance = self.getHeight(node.right) - self.getHeight(node.left)
        if -1 <= balance <= 1:
            return True
        else:
            return False
        pass
            
            
                
        



def run_tests():
    import doctest
    doctest.testmod(verbose=True)
    
if __name__ == "__main__":
    run_tests()