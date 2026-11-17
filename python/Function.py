# call
def mul(a,b):
  return a*b

print(mul(10,20)) # 200


# Type Hints
def add(a:int , b:int) ->int:  # hint only
  return a+b

print(add('Hello',' World!')) # Hello World!


# Keyword Arguments
def introduce(name, age):
    print(name, age)

introduce(age=18, name="Tom") # Tom 18


# 回傳多個值
def calculate(a,b):
  return a+b,a*b,a-b

x,y,z=calculate(2,3)
print(x,y,z) # 5 6 -1


# Default Arguments (預設)
def person(name,age=18):
  '''
  一般參數不能放在預設參數之後。
  def test(a=10, b):
    return a + b
    這會產生 SyntaxError。
  '''
  print(name,age) 

person('Tom') # Tom 18
person('Jack',20) # Jack 20


#  *args ---> 接收不定數量的位置引數
#  args 是 Tuple
def ar(*args):
  print(*args) # 20 30 40 50 60

ar(20,30,40,50,60)

#  args 是 Tuple
def ar_t(*args):
  count=0
  for i in args:
    count+=i
  return count

print(ar_t(10,20,30,40)) # 100


# **kwargs ---> 接收不定數量的關鍵字引數
def introduce(**kwargs):
    print(kwargs) # {'name': 'Tom', 'age': 18, 'major': 'CS'}

introduce(name="Tom", age=18, major="CS")

# kwargs 是 Dictionary
def introduce_d(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}") # name: Tom  age:18  major:CS

introduce_d(name="Tom", age=18, major="CS")








#end
