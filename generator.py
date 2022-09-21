import random

def generator1():
    while True:
        yield {"sep":random.randint(1600,2800), "count":random.randint(4,8)}

def generator2():
    x=input()
    gen1=generator1()
    while True:
        if x=="DOSC":
            return False
        gen=next(gen1)
        for i in range(gen['count']):
            for  j in x:
               print(j, end=" ")
               print(chr(gen['sep']),end=" ")
            print(';'*gen['count'], end="")
        print()
        x=input()
        
generator2()

