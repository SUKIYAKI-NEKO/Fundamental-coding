# creat list
arr=[10, 20, 30, 40, 50]
print(arr) #output: [10,20,30,40,50]


#Indexing
print(arr[1]) #output: 20
print(arr[-1]) #output: 50
'''
element       : 10  20  30  40  50
positive index:  0   1   2   3   4
negative index: -5  -4  -3  -2  -1
'''


# change element
arr[0]=100
print(arr) #output: [100,20,30,40,50]


#Add element

#append(x) --->在最後新增一個元素
arr.append(10)
print(arr) # [100, 20, 30, 40, 50, 10]
arr.append([10,20])
print(arr) # [100, 20, 30, 40, 50, 10, [10, 20]]

#insert(i,x) --->在指定索引插入元素
arr.insert(1,15)
print(arr) # [100, 15, 20, 30, 40, 50, 10, [10, 20]]

#extend(iterable)  --->將另一個可迭代物件的元素加入
arr.extend([20,30,40])
print(arr) # [100, 15, 20, 30, 40, 50, 10, [10, 20], 20, 30, 40]


#Remove element
#remove(x)	---> 刪除第一個值為 x 的元素
arr.remove(20)
print(arr) # [100, 15, 30, 40, 50, 10, [10, 20], 20, 30, 40]

#pop(i)	---> 刪除指定索引的元素，並回傳該元素
x=arr.pop(6)
print(x) # [10, 20]
print(arr) # [100, 15, 30, 40, 50, 10, 20, 30, 40]

#clear()  ---> 清空整個 List
arr.clear()
print(arr) # []



arr=[10,20,30,20]
#List length and search

#len() ---> 計算元素數量。
print(len(arr)) # 4

#in ---> 判斷是否存在。
print(20 in arr) # True
print(50 not in arr) # True
#index() ---> 取得元素第一次出現的位置。
print(arr.index(20)) # 1

#count() ---> 計算元素出現次數。
print(arr.count(20)) # 2


#List Slicing
arr=[10,20,30,40,50]
print(arr[1:4]) # [20, 30, 40]
'''
list[start:stop:step]
numbers[start:stop]	    索引 start 到 stop
numbers[:stop]	        從開頭到索引 stop
numbers[start:]	        從索引 start 到最後
numbers[:]	            複製整個 List
numbers[::step]	        每隔一個取值
numbers[::-1]	        反轉順序
'''
print(arr[::-1]) # [50, 40, 30, 20, 10]


'''
list()
它可以把其他可迭代物件（Iterable）轉換成串列。
'''

# 將字串轉換成串列
x="123456"
print(list(x)) # ['1', '2', '3', '4', '5', '6']

#將 map 轉換成串列

arr = ['10', '20', '30']

x = map(int, arr)
y = list(x)

print(y) # [10,20,30]
print(type(y)) # <class 'list'>







#end
