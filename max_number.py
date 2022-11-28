import random
rand_list=[]
for i in range(15):
    rand_list.append(random.randint(1,100))
max_number=max(rand_list)
print(rand_list)
print(max_number)