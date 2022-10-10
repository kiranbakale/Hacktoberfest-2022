first_name= input('What is Your First Name : ')
last_name = input('What is Your Last Name : ')
full_name = [first_name ,' ',last_name] 
i=reversed(full_name)
for x in i :
    print(x, end="")