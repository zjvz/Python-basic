class Przedział :
    def __init__(self, lewy, prawy):
        self.l=lewy
        self.p=prawy
    def __str__(self):
        if self.p<self.l:
            return f"[]"
        return f"[{self.l},{self.p}]"
    def __repr__(self):
        return f"Przedział({self.l},{self.p})"
    def __len__(self):
        if self.p<self.l:
            return 0
        return self.p-self.l
    #przeciecie przedzialow, zwraca reprezentujacy go obiekt typu Przedział
    def __and__(self,other):
        prawy=0
        lewy=0
        if self.p<self.l:
            return Przedział(0,0)
        if other.p<other.l:
            return Przedział(0,0)
        
        if other.l>=self.l and other.l<=self.p:
            lewy=other.l
            if other.p<=self.p:
                prawy=other.p
            else:
                prawy=self.p
        elif other.p<=self.p and other.p>=self.l:
            prawy=other.p
            if other.l>=self.l:
                lewy=other.l
            else:
                lewy=self.l
        else:
            return Przedział(0,0)
        return Przedział(lewy,prawy)
    #czesc wspolna, zwraca obiekt reprezentujacy ich sume, w przeciwnym wypadku generuje wyjatek
    def __add__(self,other):
        prawy=0
        lewy=0
        if self.p<self.l:
            raise ValueError()
        if other.p<other.l:
            raise ValueError()
        
        if other.l>=self.l and other.l<=self.p:
            lewy=self.l
            if other.p>self.p:
                prawy=other.p
            else:
                prawy=self.p
        elif other.p<=self.p and other.p>=self.l:
            prawy=self.p
            if other.l<self.l:
                lewy=other.l
            else:
                lewy=self.l
        else:
            raise ValueError()
        return Przedział(lewy,prawy)
#pochodna po klasie Przedział, której instancje maja dodatkowy atrybut: wspolrzedna
#w drugim wymiarze(poziom)
class Przedział2D(Przedział):
    def __init__(self,lewy,prawy,poziom):
        Przedział.__init__(self,lewy,prawy)
        self.poz=poziom
    def __str__(self):
        y=Przedział.__str__(self)
        return f"<{self.poz}>,<{y}>"
    def __repr__(self):
        return f"Przedział2D({self.l},{self.p},{self.poz}"
    #przeciecie przedzialow na roznym poziomie jest zawsze puste
    def __and__(self,other):
        if isinstance(other,Przedział):
            x=1
            return Przedział.__and__(self,other)
        else:
            if self.poz!=other.poz:
                return Przedział2D(0,0,0)
            x=0
          
        prawy=0
        lewy=0
        if self.p<self.l:
            return Przedział2D(0,0,0)
            
        if other.p<other.l:
            return Przedział2D(0,0,0)
        
        if other.l>=self.l and other.l<=self.p:
            lewy=other.l
            if other.p<=self.p:
                prawy=other.p
            else:
                prawy=self.p
        elif other.p<=self.p and other.p>=self.l:
            prawy=other.p
            if other.l>=self.l:
                lewy=other.l
            else:
                lewy=self.l
        else:
            return Przedział2D(0,0,0)
        return Przedział2D(lewy,prawy,self.poz)   
    def __add__(self,other):
        if isinstance(other,Przedział):
            x=1
            return Przedział.__add__(self,other)
        else:
            if self.poz!=other.poz:
                raise ValueError()
            x=0
            
        prawy=0
        lewy=0
        if self.p<self.l:
            raise ValueError()
        if other.p<other.l:
            raise ValueError()
        
        if other.l>=self.l and other.l<=self.p:
            lewy=self.l
            if other.p>self.p:
                prawy=other.p
            else:
                prawy=self.p
        elif other.p<=self.p and other.p>=self.l:
            prawy=self.p
            if other.l<self.l:
                lewy=other.l
            else:
                lewy=self.l
        else:
            raise ValueError()
        return Przedział2D(lewy,prawy,self.poz)
    
