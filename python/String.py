text="Hello World!"

# 字串切片
print(text[0])     # H
print(text[-1])    # !
print(text[0:3])   # Hel
print(text[::-1])  # !dlroW olleH


#Other

print(text.lower()) # hello world!
print(text.upper()) # HELLO WORLD!
print(text.title()) # Hello World!
print(text.replace("World", "Python")) # Hello Python!


# split() ---> 將字串拆成 List。
fruit='apple,banana,orange'
text=fruit.split(',')
print(text) # ['apple', 'banana', 'orange']

# join() ---> 將 List 的字串組合起來。
j=','.join(text)
print(j) # apple,banana,orange






#end
