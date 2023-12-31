# 1_4 Getting data in python

with open('doc1.txt', 'r') as file:
    data = file.read()

with open('doc1.txt', 'a')as file:
    file.write("hello")
print("Succesfully printed text in file")
