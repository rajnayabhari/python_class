# sort(reverse=True,key=Function)method
a=[2,1,10,5,12,6,7]
a.sort()
print(a)#[1, 2, 5, 6, 7, 10, 12]

a.sort(reverse=True)
print(a)#[12, 10, 7, 6, 5, 2, 1]

a=[(5,4),(3,2),(4,10),(12,1),(1,9)]

def get_second_num(data):
    return data[1]#here 1 is the index for second item

a.sort(key=get_second_num)

print(a)#[(12, 1), (3, 2), (5, 4), (1, 9), (4, 10)]

# -------------------#
a=[(4,12,5),(6,1),(11,12),(6,7,8)]

def last_num(data):
    return data[-1]#[(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)] #here -1 is the index of last item

a.sort(key=last_num)
print(a)
