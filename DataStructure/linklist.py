class Node:
    def __init__(self, value):
        '''
        Obtained Node data
        '''
        self.data = value
        self.next = None

    def getData(self):
        '''
        get data to insert into list
        '''
        return self.data

    def getNext(self):
        '''
        get next linked list value
        '''
        return self.next

    def setData(self, value):
        '''
        add data to the linked list
        '''
        self.data = value

    def setNext(self, value):
        '''
        set value to next Node list
        '''
        self.next = value

class LinkedList:
    def __init__(self):
        '''
        Initially point to head with None
        '''
        self.head = None

    def isEmpty(self):
        '''
        check wheather linked list is empty or not
        and return True if Empty else return False
        '''
        return self.head is None

    def add(self, item):
        '''
        add item to linked list
        '''
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def printlist(self):
        '''
        print the whole linked list
        '''
        current  = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()
    
    def search(self,item):
        '''
        search item in linked list
        '''
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext() 
        return found
    
    def size(self):
        '''
        returned the size of linked list
        '''
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current= current.getNext()
        return count

    def insert(self , position , item):
        '''
        insert item into linked list at given index
        '''
        if position > self.size() - 1: 
            raise IndexError ("Index out of bounds.")
        current = self.head 
        previous = None 
        pos = 0 
        if position is 0: 
            self.add(item)
        else:
            new_node = Node(item) 
            while pos < position: 
                pos += 1 
                previous = current 
                current = current.getNext()
            previous.setNext(new_node) 
            new_node.setNext(current)

    def index(self, item): 
        """
        Return the index where item is found.
        If item is not found, return None. """
        current = self.head 
        pos = 0 
        found = False 
        while current is not None and not found: 
            if current.getData() is item: 
                found = True
            else:
                current = current.getNext() 
                pos += 1
        if found: 
            pass
        else: 
            pos = None
        return pos
    def pop(self, position = None): 
        """If no argument is provided, return and remove the item at the head. If position is provided, return and remove the item at that position.
        If index is out of bounds, raise IndexError """ 
        if position > self.size():
            raise IndexError('Index out of bounds')
        
        current = self.head 
        if position is None: 
            ret = current.getData() 
            self.head = current.getNext()
        else:
            pos = 0 
            previous = None 
            while pos < position: 
                previous = current 
                current = current.getNext() 
                pos += 1 
                ret = current.getData()
            previous.setNext(current.getNext())
        print (ret)
        return ret
    def append(self, item):
        """Append item to the end of the list""" 
        current = self.head 
        previous = None 
        pos = 0 
        length = self.size() 
        while pos < length: 
            previous = current 
            current = current.getNext() 
            pos += 1
        new_node = Node(item) 
        if previous is None: 
            new_node.setNext(current) 
            self.head = new_node
        else: 
            previous.setNext(new_node)

ll = LinkedList()
ll.add('a')
ll.add('b')
ll.add('c')
ll.insert(2,'f')
ll.append(2)
ll.pop(2)
ll.printlist()


print('Required values \n')
print(ll.size())
print(ll.search('a'))
