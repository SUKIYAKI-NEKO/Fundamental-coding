#Create 
student={
  "name":"Tom",
  "age":18,
  "score":96
}


# access value
print(student["name"]) # Tom
print(student["age"]) # 18


# Add and modify
student["ID"]=123456
student["score"]=60

print(student) # {'name': 'Tom', 'age': 18, 'score': 60, 'ID': 123456}



# delete
del student['ID']
score = student.pop("score")
print(score) # 60
print(student) # {'name': 'Tom', 'age': 18}


# Other

#keys()	---> 取得所有 Key
print(student.keys()) # dict_keys(['name', 'age'])

#values() ---> 取得所有 Value
print(student.values()) # dict_values(['Tom', 18])

#items() ---> 取得 Key-Value 配對
print(student.items()) # dict_items([('name', 'Tom'), ('age', 18)])

#get(key) ---> 取得 Value，不存在時預設回傳 None
print(student.get('name')) # Tom

#pop(key) ---> 刪除指定 Key 並回傳 Value
x=student.pop('age')
print(x) # 18
print(student) # {'name': 'Tom'}

# update() ---> 更新字典
student.update()


# 遍歷 Dictionary
student = {
    "name": "Tom",
    "age": 18,
    "score": 90
}

# 只取得 Key
for key in student:
  print(key) # name age score

# 取得 Value
for value in student.values():
  print(value) # Tom 18 90

# 同時取得 Key 和 Value
for key,value in student.items():
  print(key,value) # name Tom age 18 score 90





#end
