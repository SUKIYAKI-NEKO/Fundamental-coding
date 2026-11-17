#range(stop)
for i in range(5):
  print(i,end=" ")
# 0 1 2 3 4

#range(start,stop)
for i in range(2,10):
  print(i,end=" ")
# 2 3 4 5 6 7 8 9

#range(strat,stop,step)
for i in range(0,10,2):
  print(i,end=" ")
# 0 2 4 6 8

#遍歷資料
arr=[10,20,30]
for i in arr:
  print(i)
# 10 20 30

#break
for i in range(10):
    if i == 5:
        break
    print(i)
# 0 1 2 3 4 

#continue
for i in range(5):
    if i == 2:
        continue
    print(i)
# 0 1 3 4

# Loop else
for i in range(5):
    print(i)
else:
    print("Loop finished")
# 0 1 2 4 5 Loop finished
