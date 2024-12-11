                                  #variables
       #1:string

name = "Nina ricky"
date = 5
text = f" Hello {name} you are the  beautifull girl ever"
# print(name)
# print(date)
# print(len(text))#lenth
print(text)
# print(name.upper)

        #2:list       
home =["dog","house",32, "net"]
print(home)
#printing only one item/specific item in the list 
Home = home[3]
print(Home)
# home.append("bingo")// append used to add one item in the list
home.extend(["gibson","shedy","mark","david"])#extend is to add mutiple  items
home.pop(2)
#or also  we can remove this using {home.remove(32)}
print(home)

      #3 Tuples
my_fruit =("apple","banana","mango","melon")
print(my_fruit)      
print(my_fruit[2]) 
      
numbers = (1,3,2)
number2 = (4,5,6)
num_combine = numbers + number2
print(num_combine)

       #4 set
       # unordered collection of unique items(no dublicate)
my_set = {"moky", "njoroge","micky","martin"}
print(my_set)
my_set.add("jymy")
print(my_set)

#using sorted to arreng in order
my_set2 = set([2,7,5,9,1,3])
print(sorted (my_set2))


                #5 dictionary
# its a collection of a keyvalued  pairs
my_dicti ={
    "name": "nina",
    "age" : 21,
    "gande" :"f"
 }
print(my_dicti)




