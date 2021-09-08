#list
x = [1, 2, 3, 4, 5, 6, 7]
for f in range(7) :
    print(x[f])
    
y = ["aku", "adalah", 'anak', 'sehat']
for i in range(4) :
    print(y[i])

z = [1, "aku" , 2.0, "aiodaw"]
for n in range (4) :
    print(z[n])

print(x[0])
print(y[1])
print(z[2])


#adding list
names = ["budi", 'tono', 'badut']
print(names)

#adding now
names.append("hazel")
print(names)

#adding with style (buat naruh secara teratur misalnya naruh diawal)
names.insert(1, "feli")
print(names)

#remove
names.remove("feli")
print(names)

#reverse order
names.reverse()
print(names)

x.reverse()
print(x)

#sort
numbers = [1, 9, 6, 2, 4, 3, 7, 5, 8]
numbers.sort()
print(numbers)


