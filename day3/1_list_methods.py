# Append()
vowels=["a","e","i","o"]
vowels.append("u")
print(vowels)#['a', 'e', 'i', 'o', 'u']


# extends
a=[1,2,3]
b=[4,5,6]
result=a.extend(b)
print(result)#it returns none
print(a)#[1,2,3,4,5,6]

#insert(index,value)
vowels=["a","e","o","u"]
vowels.insert(2,"i")
print(vowels)


# remove(value)
a=[1,2,3,4,5]
a.remove(3)
#a.remove(6)  #It raises value error
print(a)


#pop(index)
vowels=["a","e","i","o","u"]
result=vowels.pop(3)#i is poped from list
print(result)#i
print(vowels)#["a","e","o","u"]
#pop()method doesnot necessarily take a parameter.If parameter is not provided then last item is poped form the list


#clear()
a=[1,2,3]
a.clear()#remove all elements in list
print(a)

#index(value,start,end)
vowels=["a","e","i","o","u"]
result=vowels.index("i")
print(result)

a=[1,2,3,4,1,4,5,2,3,2]
result=a.index(2,2)
print(result)#7

result=a.index(2,1,7)
print (result)#2 cannot be found in list

result=a.index(1,2,8)
print(result)#1 found in 4th position


#count
a=[1,2,3,4,1,4,5,2,3,2]
print(a.count(3))#2
print(a.count(2))#3


#reverse()
a=[2,1,10.9,3]
a.reverse()
print(a)#[3, 10.9, 1, 2] only item are reversed not sorted
