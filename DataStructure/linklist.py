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
        and retunr True if Empty else return False
        '''
        return sef.head is None

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

ll = LinkedList()
ll.add('a')
ll.printlist()
print(ll.size())
print(ll.search('a'))