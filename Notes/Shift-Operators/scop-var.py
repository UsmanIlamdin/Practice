var = 1


def nust():
    '''
    test local and global variable present
    '''
    num = 1
    print(locals().keys())
    print(globals().keys())


nust()


# change global inside function
var = 2


def changeglobal():
    '''
    change global in local
    '''
    global var
    var = 30


changeglobal()
print(var)

foo = 0  # global foo
def f1(): 
    foo = 1  # a new foo local in f1
    def f2(): 
        foo = 2  # a new foo local in f2  
        def f3(): # a new foo local in f3 
            print(foo) # 3 
            foo = 30 # modifies local foo in f3 only
            foo = 3
            def f4(): 
                global foo 
                print(foo)  # 0 foo = 100 # modifies global foo
