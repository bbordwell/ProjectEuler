#This program Solves Project Euler #61.

class FigurateNumber:
    """This class represents a figurate number and supports addition if they are cyclical"""
    def __init__(self,n,shape):
        self.n = str(n)
        if shape == 'octagonal':
            self.octagonal = True
        else:
            self.octagonal = False
        if shape == 'heptagonal':
            self.heptagonal = True
        else:
            self.heptagonal = False
        if shape == 'hexagonal':
            self.hexagonal = True
        else:
            self.hexagonal = False
        if shape == 'pentagonal':
            self.pentagonal = True
        else:
            self.pentagonal = False
        if shape == 'square':
            self.square = True
        else:
            self.square = False
        if shape == 'triangle':
            self.triangle = True
        else:
            self.triangle = False
        
        
    def __add__(self,other):
        if self.n[-2:] != other.n[:-2]:
            raise ValueError
            
        if (self.square and other.square) or (self.triangle and other.triangle) or (self.pentagonal and other.pentagonal) or (self.hexagonal and other.hexagonal) or (self.heptagonal and other.heptagonal) or (self.octagonal and other.octagonal) :
            raise ValueError
        
        new = FigurateNumber(self.n+other.n,None)
        if self.square or other.square:
            new.square = True
        if self.triangle or other.triangle:
            new.triangle = True
        if self.pentagonal or other.pentagonal:
            new.pentagonal = True   
        if self.hexagonal or other.hexagonal:
            new.hexagonal = True
        if self.heptagonal or other.heptagonal:
            new.heptagonal = True
        if self.octagonal or other.octagonal:
            new.octagonal = True
        return new
        
    def __str__(self):
        return self.n

octagonals = [x*(3*x - 2) for x in range(19,59)]
octagonals = [FigurateNumber(x,'octagonal') for x in octagonals]
heptagonals = [x*(5*x - 3)//2 for x in range(21,64)]
heptagonals = [FigurateNumber(x,'heptagonal') for x in heptagonals]
hexagonals = [x*(2*x -1) for x in range(23,71)]
hexagonals = [FigurateNumber(x,'hexagonal') for x in hexagonals]
pentagonals = [x*(3*x -1)//2 for x in range(26,82)]
pentagonals = [FigurateNumber(x,'pentagonal') for x in pentagonals]
squares = [x**2 for x in range(32,100)]
squares = [FigurateNumber(x,'square') for x in squares]
triangles = [x*(x+1)//2 for x in range(45,141)]
triangles = [FigurateNumber(x,'triangle') for x in triangles]
cyclicals = [x for x in octagonals]
figurateNumbers = heptagonals + hexagonals + pentagonals + squares + triangles

def appendFigurate(cyclicals,figurateNumbers):
    """Input a list known cyclical numbers and a list of figurate numbers and output
       all valid cyclical numbers with n+1 length."""
    news = []
    for cyclical in cyclicals:
        for figurateNumber in figurateNumbers:
            try:
                news.append(cyclical+figurateNumber)
            except ValueError:
                pass
    return news

for i in range(5):
    cyclicals = appendFigurate(cyclicals,figurateNumbers)

def doesWrap(cyclicals):
    """Input a list of cyclical numbers and output only ones that wraap around
       from end to beginning."""
    news = []
    for cyclical in cyclicals:
        if cyclical.n[-2:] == cyclical.n[:2]:
            news.append(cyclical)
    return news
    
cyclicals = doesWrap(cyclicals)
print(int(cyclicals[0].n[0:4]) + int(cyclicals[0].n[4:8]) + int(cyclicals[0].n[8:12]) + int(cyclicals[0].n[12:16]) + int(cyclicals[0].n[16:20]) + int(cyclicals[0].n[20:]))
    


    


    




        
    