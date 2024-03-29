#!/usr/bin/env python
# coding: utf-8

# In[1]:


#global vars   
MAX_B_LEN = 20
MAX_u_LEN = 10
 
books=list()  
users=list()  
 
import re 
class Books : 
  def __init__(self) :  
    self.name =str()
    self.id =str()
    self.quantity=int() 
    self.brd=int() 
    self.u_b=list()
  def AddBook(self , name , id , qunt , br=0 ) : 
         self.name = name 
         self.id = id 
         self.quantity = qunt  
         self.brd=br 
         books.append(self)  
         print("Book added :)")
 
 
  def PrintBooks(self) :     
    for i in range(len(books)):   
      print("Book Name : ",books[i].name.ljust(MAX_B_LEN), "-ID :", books[i].id , "  -Quantity :" ,books[i].quantity ,"  -borrowed : ",books[i].brd )    
 
  def PrintByprf(self , prfx  ) :   
    f = 0
    for i in books :  
      ptr = r'(^'+prfx+')'
      m = re.match(ptr , i.name) 
      if m :  
          f = 1 
          print(i.name.ljust(MAX_B_LEN), "-ID :", i.id , "-Quantity :" ,i.quantity ,"-borrowed : ", i.brd )      
      if (not f) : print("no such book ")         
 
 
 
  def print_book_users(self ,bnm , bid) : 
    f=1 
    f1=1
    self.name = bnm 
    self.id =bid 
    for i in books : 
      if(self.id == i.id and self.name == i.name) : 
        f=0
        print("users: ")
        for x in i.u_b :
          f1=0 
          print(x)
    if(f): print("no such book") 
    if(f1): print("no body borrowed that book")
 
 
 
 
 
 
 
 

class User : 
  def __init__(self ) : 
    self.b_l =list() 
    self.id =str()
    self.name ="user"
 
  def adduser(self , nm , id) :
    self.name = nm 
    self.id = id    
    users.append(self) 
 
  def  PrintUsers(self) :   
    for i in users : 
       print(i.name.ljust(MAX_u_LEN), "-ID :", i.id )  
       if(len(i.b_l) >0 ) :
          print("borrowed books : ") 
          for j in  i.b_l :  
             print("book name : ", j.name.center(MAX_u_LEN) , "   -id: ",j.id )  
 
    
 
  def borrow(self , bnm , bid, unm , uid) :  
 
       bb=Books() 
       bb.name = bnm 
       bb.id = bid 
       f1 = 1 
       f2= 1 
       f3 = 1 
       for i in books :   
          if(i.id == bb.id and i.name == bb.name)  : 
            f1=0 
            if(int(i.quantity) > 0 ) :  
              f2=0  
              uu=User() 
              uu.name = unm  
              uu.id =uid  
              for x in users : 
               if(x.name == uu.name and x.id == uu.id) :  
                 f3=0  
                 i.quantity -=1 
                 i.brd +=1  
                 i.u_b.append(uu.name) 
                 x.b_l.append(bb)  
 
       if(f1 or f2 or f3) : 
          return 0 ; 
       return 1 ;          
                  
              
                  
  def  Retrn(self , bnm , bid , unm , uid) :    
        bb=Books() 
        bb.name = bnm 
        bb.id = bid 
        f1 = 1 
        f2= 1
        f3 = 1 
        
        for b in books :   
          if(b.id == bb.id and b.name == bb.name)  : 
            f1=0 
            uu=User() 
            uu.name = unm  
            uu.id =uid  
            for x in users : 
               if(x.name == uu.name and x.id == uu.id) :  
                 f2=0  
                 b.quantity +=1 
                 b.brd -=1  
                 b.u_b.remove(bb.name) 
                 for k in x.b_l :  
                   if(k.name == b.name and k.id == b.id) :
                      f3=0
                      x.b_l.remove(k)
                   
                  
            if(f1 or f2 or f3 ) : 
               return 0 ; 
            return 1 ;       
            
 

import random as rnd 
class Data : 
   u_names= ["maha" , "dina" , " youmna" ,"khaled" , "ahmed" , "mostafa" , "amin" , "ali" , "ayman" , "sayed" , "alaa" , "donuia" , "rana" , "salma" ] 
   #u_names = list([ x.capitalize()  for x in u_names])
   b_names =["harryputer" , "blackbpne" , "satrve" , "stive jobs" , "the blussem" , "c++ for dummies" , "java" , "tensorflow steps" , "python for beginners " , "software engineering  tips" , "algo for AI" , "danial drain " , " fun stories " ,"kids edu" ,"baby bird"  ] 
   #b_names = list([ x.capitalize()  for x in b_names])
   
 
 
   for i in  range(len(u_names)):  
       u = User() 
       u.name = u_names[i] 
       u.id = u_names[i][0]+'2022'+str(i)+'U'
       users.append(u) 
 
 
   for i in range(0,len(b_names)) : 
     b=Books() 
     b.name = b_names[i] 
     b.id =  b_names[i][0]+'2022'+str(i)+'B'
     b.quantity=i+10
     b.brd = i+1
     books.append(b) 
 
     # insert in  b_l , u_b  
     k = 0 
     for i in users : 
       for m in range(k , k+1):
        i.b_l.append(books[m])
        books[m].quantity-=1
        if(books[m].quantity<=0) :
          break
        books[m].brd+=1
        books[m].u_b.append(i.name)
        k+=3  
        if(k >=len(books)): 
          k=0;
        
      
     
 
   for i in books : 
          print("Book Name : ",i.name.ljust(MAX_B_LEN), "-ID :", i.id , "  -Quantity :" ,i.quantity ,"  -borrowed : ",i.brd )     
          if (len(i.u_b)) : 
            print(i.u_b)
 
 
   print(len(u_names)) 
   print(len(b_names))     
 
 
   
 
      
 

u = User() 
u.name = 'maha'
u.id ="22" 
if(u in users): 
  print(1) 
else : 
  print(0)   
 
for i in users : 
  if(i.name == u.name and i.id == u.id ) : 
    print(i.name , i.id)

if __name__ == '__main__' :  
 s = """ 
 
 choose an option : 
1)Add Book  
2) Pint Library Books 
3) Print Books By Prifix 
4) Add user 
5) print users borrowed a book
6) return book 
7) borrow book 
8) print users 
9)end program
 
 
 """   
 b = Books() 
 u = User() 
 print(s)  
 
 
 while(ch !=9) :  
 
  ch = int(input() )
 
  if(ch == 1 ):     
    print("enter book name : ")  
    nm= input()
    print("enter book id : ")  
    id =input()
    print("enter book quanitiy : ")  
    q= int(input() )
    b.AddBook(nm , id , q , 0 ) 
 
 
  elif (ch == 2) :   
 
   b.PrintBooks()
 
  elif (ch == 3) :  
   
    print("Enter book prfx : ") 
    prfx = input()   
    b.PrintByprf(prfx)
 
  elif (ch == 4) :    
    print("Enter user name : ")  
    nm = input()   
    print("Enter book id : ") 
    id= input()   
 
    u.adduser(nm, id )
    print("user added :>")
  elif (ch == 5) :  
   print("Enter book  name  : ") 
   bnm = input()   
   print("Enter book id  : ") 
   bid = input()     
   b.print_book_users(bnm , bid)
  elif (ch == 6) : 
   print("Enter book name  : ") 
   nm = input()   
   print("Enter book id  : ") 
   id = input()     
   print("Enter User name  : ")  
   unm = input()   
   print("Enter User id  : ") 
   uid = input()   
   
   if( u.Retrn(bnm , bid , unm , uid ) ) : 
          print("Thanks =)")     
   else :      
         print("return fails :|")     
     
   
 
  elif (ch == 7) :   
    print("Enter book name  : ") 
    bnm = input()   
    print("Enter book id  : ") 
    bid = input()   
      
    print("Enter User name  : ")  
    unm = input()   
    print("Enter User id  : ") 
    uid = input()   
   
    if( u.borrow(bnm , bid , unm , uid ) ) : 
          print("Enjoy =)")     
    else :      
         print("you cant borrow that book :|")     
     
  elif (ch == 8) : 
    u.PrintUsers()   
 
  elif (ch == 9 ): 
     break; 
  print(s)  
   
 
 


# In[ ]:




