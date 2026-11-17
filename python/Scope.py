def local():
  a=10 #Local Variable
  print(a) # 10

local()


x = 100 # Global Variable

def text0():
  print(x) # 100
def test():
  global x # 在函式內修改全域變數
  '''
  global x 必須在函式內第一次使用 x 之前宣告。
  '''
  x = 20 
  print(x) # 20

text0()
test()


#end
