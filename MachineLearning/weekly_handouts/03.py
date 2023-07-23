num_list = [1,2,3,4,5,6]
for i in range(len(num_list)):
    for j in range(i):
        print(num_list[j], end ='')
    print("")