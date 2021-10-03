class Node:
    def __init__(self,value):
        "Create Node with value and None pointer"
        self.data=value
        self.next=None
    
    def getData(self):
        "Get Node data"
        return self.data

    def getNext(self):
        "get next Node"
        return self.next

    def setData(self,value):

        self.data=value
    
    def setNext(self,value):
        self.next=value

class LinkedList:
    def __init__(self):
         self.head=None

    def isEmpty(self):
        return self.head is None

    def addValue(self,value):
        new_node = Node(value)
        new_node.setNext(self.head)
        self.head=new_node
 
    def PrintList(self):
        current=self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

    def findNthfromEnd(self,N):
        temp0 = self.head
        count=0
        while temp0 is not None:
            count +=1
            temp0 = temp0.getNext()
        print(count)
        temp1 = self.head
        for i in range(count-N):
            temp1=temp1.getNext()
        print(temp1.getData())


L_L=LinkedList()
L_L.addValue(34) 
L_L.addValue(4) 
L_L.addValue(43) 
L_L.addValue(56) 
L_L.addValue(876) 
L_L.addValue(23) 

#print(L_L.isEmpty()) 



L_L.PrintList()
print("\n \n")

L_L.findNthfromEnd(2)