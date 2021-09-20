problems = 'nerd, pale, broke, fool'
print(problems)

#split digunakan untuk mengubah sebuah string menjadi list

l = problems.split(", ")
print(l[3])

for x in range(4) : 
    print (l[x])
   
#join untuk mengubah list menjadi strings
joined = ''.join(l)

print(joined)
