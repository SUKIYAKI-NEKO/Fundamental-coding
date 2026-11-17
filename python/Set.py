'''
元素不重複。
不保證固定的元素順序。
不支援透過索引存取元素。
'''

#Creat
arr={10,30,20,40,20,10,30}
print(arr) # {40, 10, 20, 30}


# Add and Remove

# add(x) ---> 新增元素
arr.add(50)
print(arr) # {40, 10, 50, 20, 30}

# remove(x) ---> 刪除元素，不存在會報錯
arr.remove(40)
print(arr) # {10, 50, 20, 30}

# discard(x) ---> 刪除元素，不存在不會報錯
arr.discard(10)
print(arr) # {50, 20, 30}

# pop() ---> 移除並回傳隨機一個元素
x=arr.pop()
print(x) # 50
print(arr) # {20, 30}

# clear() ---> 清空集合
arr.clear()
print(arr) # set()


#集合運算
a={0,1,2,3,4,5}
b={2,3,4,5,6,7}

#Union
print(a | b) # {0, 1, 2, 3, 4, 5, 6, 7}

#Intersection
print(a & b) # {2,3,4,5}

#Difference
print(a-b) # {0,1}
print(b-a) # {6,7}

#（Symmetric Difference
print(a ^ b) # {0,1,6,7}







#end
