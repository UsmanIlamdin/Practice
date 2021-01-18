def f(a, b=42, c=[]): 
    pass
print(f.__defaults__) # Out: (42, [])