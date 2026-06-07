class Prime:
    def __init__(self):
        self.pr=[]
        self.start=2
        self.pairs=[]
    def Prime_Generator(self,lim:int):        
        for i in range(self.start,lim+1):
            b=1
            for j in self.pr: 
                if(j>i**0.5 + 1):
                    break
                if(i%j==0):
                    b=0
                    break
            if(b):
                self.pr.append(i)
        self.start=lim+1
        return self.pr
    def __Prime_Sorter__(self):
        pass
    def Prime_Pair(self):
        