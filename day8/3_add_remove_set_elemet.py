#add
s={1,2,3}
s.add(4)
print(s)

# Update
s={1,2,3}
s.update([4,5,6])
print(s) #{1,2,3,4,5,6}

#remove
s={1,2,3,4,5,6}
s.remove(4)
print(s)#{1, 2, 3, 5, 6}
# s.remove(8)
# Print(s) #It raises error

# discard
s={1,2,3,4,5,6}
s.discard(5)
print(s)#{1, 2, 3, 5, 6}
s.discard(8)
print(s)

#pop
s={1, 2, 3, 5, 6}
s.pop()
print(s) #randomly pops any one element from the set

# Clear
s={1, 2, 3, 5, 6}
s.clear()
print(s) #{}

