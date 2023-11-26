a = [11,1,3,3,4,6]
type1 = type(a)
# print(type(a))

if(type(a) == int):
    print("Integer")

if(type(a) == float):
    print("Float")

if(type(a) == bool):
    print("Bool")

if(type(a) == str):
    print("String")

if(type(a) == list):
    print("List")

if(type(a) == None):
    print("None")

b = [100,9,8,7]
print("A = ",a)
print("B = ",b)
c = a + b
print("C = ",c)
c.sort()
print("D = ",c)