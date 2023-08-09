# Tuple in python can be packed and unpacked

# Packing of tuple

vowels = "a", "e", "i", "o", "u"
print(vowels)  # ('a', 'e', 'i', 'o', 'u')
a = 1, 2
print(a)  # (1, 2)


# unpacking
a,b=1,2
print(a) #1
print(b) #2

a,b=(1,2)
print(a) #1
print(b) #2


# Possible errors in packing and unpacking

a,b,c=1,3 #Not enough value to unpack
a,b=1,2,3 #too many values to unpack
