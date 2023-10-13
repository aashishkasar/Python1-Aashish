def lower_(x):
    l=len(x)
    a=0
    while a<l:
        y=ord(x[a])
        if y>=65 and y<=90:
            y=y+32
            print(chr(y),end="")
        else:
            print(chr(y),end="")
        a=a+1
def upper_(x):
    l=len(x)
    a=0
    while a<l:
        y=ord(x[a])
        if y>=97 and y<=122:
            y=y-32
            print(chr(y),end="")
        else:
            print(chr(y),end="")
        a=a+1
def islower_(x):
    l=len(x)
    a=0
    b=0
    while a<l:
        y=ord(x[a])
        if y>=97 and y<=122 or  y>=48 and y<=57:
            b=b+1
        else:
            pass
        a=a+1
    if b==l:
        print("true")
    else:
        print("false")

def isupper_(x):
    l=len(x)
    a=0
    b=0
    while a<l:
        y=ord(x[a])
        if y>=65 and y<=90 or y>=48 and y<=57:
            b=b+1
        else:
            pass
        a=a+1
    if b==l:
        print("true")
    else:
        print("false")
def isalpha_(x):
    l=len(x)
    a=0
    b=0
    while a<l:
        y=ord(x[a])
        if y>=65 and y<=90 or y>=97 and y<=112 :
            b=b+1
        else:
            pass
        a=a+1
    if b==l:
        print("true")
    else:
        print("false")

def isdigit_(x):
    l=len(x)
    a=0
    b=0
    while a<l:
        y=ord(x[a])
        if y>=48 and y<=57:
            b=b+1
        else:
             pass
        a=a+1
    if b==l:
         print("true")
    else:
        print("false")
def swapcase_(x):
    l=len(x)
    a=0
    while a<l:
        y=ord(x[a])
        if y>=65 and y<=90:
            y=y+32
            print(chr(y),end="")
        elif y>=97 and y<=122:
            y=y-32
            print(chr(y),end="")
        else:
            print(chr(y),end="")
        a=a+1
def alnum_(x):
    l=len(x)
    a=0
    b=0
    while a<l:
        y=ord(x[a])
        if y>=65 and y<=90 or y>=97 and y<=122 or y>=48 and y<=57:
            b=b+1
        else:
            pass
        a=a+1
    if b==l:
        print("true")
    else:
        print("false")
def isspace_(x):
    l=len(x)
    a=0
    b=0
    while a<l:
        y=ord(x[a])
        if y==32:
            b=b+1
        else:
            pass
        a=a+1
    if b==l:
        print("true")
    else:
        print("false")
def capitalize_(x):
    l=len(x)
    a=0
    b=0
    while a<l:
        y=ord(x[a])
        if a==0 and y>=97 and y<=122:
            y=y-32
            print(chr(y),end="")
        elif a==0 and y>=65 and y<=90:
            print(chr(y),end="")
        elif a>=1 and a<len(x) and y>=97 and y<=122 :
            print(chr(y),end="")
        elif a>=1 and a<len(x) and y>=65 and y<=90:
            y=y+32
            print(chr(y),end="")
        elif y>=48 and y<=57:
            print(chr(y),end="")
        a=a+1

            
    
    

            
    
            
        
        
   
        
