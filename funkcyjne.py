#list(map(chr,range(64,181)))

L=[*"abcdefgh"]
K=range(3,3+len(L))

def X(l,k): return l*k

print(X(10,3))
print(X('10',3))
print(X(10,'3'))


print(list(map(X,L,K)))

def XX(p): return X(*p)

print(list(map(XX,zip(L,K))))


Y1=lambda p: X(*p)
print(list(map(lambda p: X(*p), zip(L,K))))

