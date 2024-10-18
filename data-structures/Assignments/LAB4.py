# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:   # You are not allowed to modify this class
    def __init__(self, value=None):  
        self.next = None
        self.value = value
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__

class Malloc_Library:

    """
    ** This is NOT a comprehensive test sample, test beyond this doctest
        >>> lst = Malloc_Library()
        >>> lst
        <BLANKLINE>
        >>> lst.malloc(5)
        >>> lst.head
        Node(None)
        >>> lst
        None -> None -> None -> None -> None
        >>> len(lst)
        5
        >>> lst[0] = 23
        >>> lst
        23 -> None -> None -> None -> None
        >>> lst[0]
        23
        >>> lst[1]
        >>> lst.realloc(1)
        >>> lst
        23
        >>> lst.calloc(5)
        >>> lst
        0 -> 0 -> 0 -> 0 -> 0
        >>> lst.calloc(10)
        >>> lst[3] = 5
        >>> lst[8] = 23
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0 -> 0 -> 0 -> 0 -> 23 -> 0
        >>> lst.realloc(5)
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0
        >>> other_lst = Malloc_Library()
        >>> other_lst.realloc(9)
        >>> other_lst[0] = 12
        >>> other_lst[5] = 56
        >>> other_lst[8] = 6925
        >>> other_lst[10] = 78
        Traceback (most recent call last):
            ...
        IndexError
        >>> other_lst.memcpy(2, lst, 0, 5)
        >>> lst
        None -> None -> None -> 56 -> None
        >>> other_lst
        12 -> None -> None -> None -> None -> 56 -> None -> None -> 6925
        >>> temp = lst.head.next.next
        >>> lst.realloc(0)
        >>> temp.next is None
        True
    """

    def __init__(self): # You are not allowed to modify the constructor
        self.head = None
    
    def __repr__(self):  # You are not allowed to modify this method
        current = self.head
        out = []
        while current:
            out.append(str(current.value))
            current = current.next
        return " -> ".join(out)

    __str__ = __repr__
    
    def __len__(self):
        # --- YOUR CODE STARTS HERE
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
        # pass  # remove when starting implementation 

    
    def __setitem__(self, pos, value):
        # --- YOUR CODE STARTS HERE
        current = self.head
        count = 0
        if pos > len(self):
            raise IndexError()
        while current is not None:
            if count == pos:
                current.value = value # set value at index
            count += 1
            current = current.next 
                
        # pass  # remove when starting implementation 


    def __getitem__(self, pos):
        # --- YOUR CODE STARTS HERE
        current = self.head
        count = 0
        while current is not None: # runs through linked list
            if count < pos:
                count += 1
                current = current.next
            elif count > pos:
                raise IndexError("Index out of range")
            else:
                return current.value # return value at index
        # pass  # remove when starting implementation 
    

    def malloc(self, size):
        # --- YOUR CODE STARTS HERE
        self.free() # resets all linked list connections
        self.head = None # makes sure the self.head is reset as well
        count = 0
        while count < size: # adds a none node according to size
            noneNode = Node(None)
            noneNode.next = self.head
            self.head = noneNode
            count += 1
        # pass  # remove when starting implementation 


    def calloc(self, size):
        # --- YOUR CODE STARTS HERE
        self.free() # when called resets the linked list.
        self.head = None # resets self.head as well
        count = 0
        while count < size: # adds zero nodes according to size
            noneNode = Node(0)
            noneNode.next = self.head
            self.head = noneNode
            count += 1
        # pass  # remove when starting implementation 


    def free(self):
        # --- YOUR CODE STARTS HERE
        current = self.head
        while current is not None:
            temp = current
            current = current.next
            temp.next = None
        # pass  # remove when starting implementation 


    def realloc(self, size):
        # --- YOUR CODE STARTS HERE
        temp = None
        if size == 0: # unallocate everything
            self.free()
        elif len(self) == 0: # create a linked list if realloc is called on an empty linked list
            self.malloc(size)
        elif size > len(self): # if the size is greater than the size of current linked list
            count = 0
            while count < (size - len(self)):
                noneNode = Node(None)
                noneNode.next = temp
                temp = noneNode
                count += 1
            current = self.head
            while current is not None:
                previous = current
                current = current.next
            previous.next = temp
        else: # if size is smaller than current linked list
            current = self.head
            count = 0
            while current is not None:
                temp = current
                current = current.next
                count += 1
                if count >= size:
                    temp.next = None
        

        # pass  # remove when starting implementation 



    def memcpy(self, ptr1_start_idx, pointer_2, ptr2_start_idx, size):
        # --- YOUR CODE STARTS HERE
        
        if ptr1_start_idx < len(self) and ptr2_start_idx < len(pointer_2):
            if size > (len(self) - ptr1_start_idx): # set size what its supposed to be if its too large
                size = (len(self) - ptr1_start_idx)
            index2 = 0
            index2 += ptr2_start_idx
            index1 = 0
            index1 += ptr1_start_idx
            while size > 0:
                pointer_2[index2] = self[index1] # uses both __getitem__ and __setitem__
                index2 += 1
                index1 += 1
                size -= 1
                
        # pass  # remove when starting implementation 
    


def run_tests():
    import doctest
    doctest.testmod(verbose=True)
     

if __name__ == "__main__":
    run_tests()