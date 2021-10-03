class Stack:
    def __init__(self): 
        self.items = []
    #method to check the stack is empty or not 
    def isEmpty(self): 
        return self.items == []
    #method for pushing an item 
    def push(self, item): 
        self.items.append(item)
    #method for popping an item 
    def pop(self): 
        return self.items.pop()
    #check what item is on top of the stack without removing it 
    def peek(self): 
        return self.items[-1]
    #method to get the size 
    def size(self): 
        return len(self.items)
    #to view the entire stack d
    def fullStack(self): 
        return self.items

def checkParenth(str): 
    stack = Stack() 
    pushChars, popChars = "<({[", ">)}]" 
    for c in str: 
        if c in pushChars: 
            stack.push(c)
        elif c in popChars: 
            if stack.isEmpty(): 
                return False
            else: 
                stackTop = stack.pop()
            # Checks to see whether the opening bracket matches the closing one 
                balancingBracket = pushChars[popChars.index(c)] 
                if stackTop != balancingBracket: 
                    return False
                else: 
                    return False 
    return not stack.isEmpty()

print(checkParenth("[]()(())({})"))