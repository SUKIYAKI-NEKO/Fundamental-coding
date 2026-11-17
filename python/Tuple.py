a=(10)
b=(10,)

print(type(a)) # <class 'int'>
print(type(b)) # <class 'tuple'>

tuple=(10,20,30)
'''
numbers[0] = 100 
----> error!!!
Tuple 建立後不能修改元素。
'''
print(tuple[0]) # 10


#Unpacking

person=("Tom",18,"Taiwan")
name,age,country=person
print(age) # 18
print(name) # Tom
print(country) # Taiwan


#Swap Element

a=10
b=20
a,b=b,a
print(a) # 20
print(b) # 10




#end
