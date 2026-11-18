'''
把某個函式套用到一個可迭代物件中的每個元素。
map() 產生的 Iterator 通常只能完整遍歷一次
map(function, iterable)
'''
# 轉換型別
arr=['10','20','30']
print(type(arr))  #<class 'list'>
arr=map(int,arr)
print(type(arr)) # <class 'map'>

#x=list(map(int,input().split()))


#使用自己定義的函式
def s(x):
  return x*x

arr=[10,20,30]
result=map(s,arr)
print(list(result)) # [100, 400, 900]


# 同時處理多個 List
a=[10,20,30]
b=[1,2,3]

re=map(lambda x,y:x+y,a,b)
print(list(re)) # [11, 22, 33]
