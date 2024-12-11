class author:
    def __init__(self, name, year ):
        self.name = name 
        self.year = year
        self.books = []
     
    def add_books(self,author):
        self.books.append(author)


class book:
    def __init__(self, pages,type):
        self.pages = pages
        self.type  =type
 

#instances 
author1 = author ("nina", "2004")

book1 = book(354,"set book ")
book2 = book(76,"jornal")
book3 = book(312,"jonal")
book4 = book(125,"set book ")
book5= book(524,"set book ")


#associate 
author1.add_books(book1)
author1.add_books(book2)
author1.add_books(book3)
author1.add_books(book4)
author1.add_books(book5)

print(f'{author1.name},{author1.year}')
print('the author who wrote this books is {name} and all books where writen in the year {year}')


for Nina in author1.books:
    print(f"amount of pages in the books:{Nina.pages} and the type of books are as  follows {Nina.type} ")





    #example 2 
class fruits:
    def __init__(self,market,home,semi):
        self.market = market
        self.home = home 
        self.semi = semi
        self.add_vagetables = []

    def add_vegatable(self,fruits):
        self.vagetables.apend(fruits)
        
class vegatabl:
    def __init__(self,adbale,nonadbale):
        self.adbale = adbale
        self.non-adbale = nonadbale 
    

##int 
fruit1 = fruits("apple","banana","mango")

Vegatable1 = vegatabl("carrot","kells")
Vegatable2 = vegatabl("cabbege","managu")
Vegatable3 = vegatabl("mooon","terere")
Vegatable4 = vegatabl("cucamber","mchicha")

#assosiat
fruit1.add_vagetables(Vegatable1)
fruit1.add_vagetables(Vegatable2)
fruit1.add_vagetables(Vegatable3)
fruit1.add_vagetables(Vegatable4)

#prints  
print(f'{fruit1.market} {fruit1.home} {fruit1.semi}');   

print(f'most of the vegs made are ')

for vagatables in fruit1.vagetables: 
    print(f'some of the vagetables are grown for : {vagatables:market} , {vagatables:home}and others are {vagatables:semi}')


#many to many relantionship
    