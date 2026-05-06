ex_8="Orange"
print(ex_8.upper())
print(ex_8[0])
print(ex_8[2])
print(ex_8[4])
print(ex_8.index("e"))
print(ex_8.count("e"))

ex_10="apricots"

print(ex_10[:3])
print(ex_10[3:])
print(ex_10[-3:])
print(ex_10[-3:-1])
print(ex_10[2:5])

print(ex_8 + "/" + ex_10)
print(ex_8,"-",ex_10)


# Exercise 

to_slice = "Just do it!"
print(to_slice)
print(len(to_slice))
print(to_slice[10])   # prints "!"
print(to_slice[5:7])  # prints "do"
print(to_slice[8:])   # prints "it!"
print(to_slice[:4])   # prints "Just"
print("Don't " + to_slice[5:])  # prints "Don't do it!"

