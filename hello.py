
#print("hello")


a =1 
b = 2

c = a+b

#print(c)

num_list = [1,2,3,4]

#print(num_list[1])

#for num in num_list:
#	print(num)

name_list = ["John", "Mary", "Tom"]

# for name in name_list:
# 	for num in num_list:
# 		print (name + str(num))

another_list = []
for num in num_list:
	another_list.append( (num+3)*2 )

# another_list2 = [(num + 3)*2 for num in num_list]

# print(another_list)
# print(another_list2)

# for num in another_list:
# 	if num > 11:
# 		print("Big number: "+str(num))
# 	elif (num <9):
# 		print("small num: "+ str(num))

def my_function():
	print("Hello World")
	print("Hello World again")
	print("Hello")

my_function()

def add_nums(num1, num2):
	return (num1 + num2) ** 2

print(add_nums(1,2))

DRY = "Don't repeat yourself"












