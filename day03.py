#lists
thislist=['menna','rahma','lala','anas']
thislist[1:3]=['lala','menna']
print(thislist)

thislist=['menna','rahma','lala','anas']
thislist[1:3]=['lala']
print(thislist)

thislist=['menna','rahma','lala','anas']
thislist.insert(2,'lala')#add to the specific index
print(thislist)

thislist.append('menna')#add to the end of the list
print(thislist)


list1=['menna','rahma','lala','anas']
list2=['mohamed','sara','hassan','mona']
list1.extend(list2)#add list2 to list1
print(list1)

list1.remove('menna')#remove specific item
print(list1)

list1.pop(2)#remove specific index
print(list1) 
   
del list1[0]#remove specific index
print(list1)

del list1#delete the entire list

list2.clear()#delete all items in the list


for x in thislist:
  print(x)  

for i in range(len(thislist)):
  print(thislist[i])
  
v=0
while v < len(thislist):
  print(thislist[v])
  v+=1  

#list comprehension
fruits=['apple','banana','cherry','kiwi','mango']
newlist=[x for x in fruits if 'a' in x]#new list with items that contain 'a'
print(newlist)
newlist=[x for x in fruits if x!='apple']#new list with items that are not 'apple'
print(newlist)
newlist=[x for x in fruits]#new list with all items in the original list
print(newlist)

newlist=[x for x in range(10)]#new list with numbers from 0 to 9
print(newlist)

newlist=['hi' for x in fruits]#new list with 'hi' for each item in the original list
print(newlist)  

#sorting lists
list3=['salma','menna','rahma','lala','anas']
list3.sort()#sort the list in ascending order
print(list3)

list3.sort(reverse=True)#sort the list in descending order
print(list3)

list4=[100,50,65,82,23]
list4.sort()#sort the list in ascending order
print(list4)
list4.reverse()#reverse the list
print(list4)


#copying lists
list5=['menna','rahma','lala','anas']
list6=list5.copy()#copy the list
print(list6)
list7=list(list5)#copy the list
print(list7)
list8=list5[:]#copy the list
print(list8)


#tuples  rounded brackets
thistuple=('menna','rahma','lala','anas')
print(thistuple)

thistuple = ("apple",)#tuple with one item must have a comma after the item
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


x=('menna','rahma','lala','anas')
print(x[0])#access the first item in the tuple
print(x[1:3])#access items from index 1 to 2
y=list(x)#convert the tuple to a list
y[1]='sara'#change the second item in the list
x=tuple(y)#convert the list back to a tuple 
print(x)

del x#delete the entire tuple

thistuple1=('menna','rahma','lala','anas')
thistuple1.count('menna')#count the number of times 'menna' appears in the tuple
thistuple1.index('lala')#return the index of the first occurrence of 'lala' in the tuple



#sets  curly brackets
thisset={'menna','rahma','lala','anas'}
mylist=['menna','rahma','lala','anas']
thisset.update(mylist)
print(thisset)








