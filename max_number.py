import random
rand_list=[]
for i in range(15):
    rand_list.append(random.randint(1,100))
max_number=max(rand_list)
print(rand_list)
print(max_number)

list = ([1,5,10,20,30,15168615,100,99,1000])
maxnumb=0
for i in list:
    if i>maxnumb:
        maxnumb=i 
print(list)
print("max number=", maxnumb)
