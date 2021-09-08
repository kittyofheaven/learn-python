#sama kaya list sama tuple tapi pake {}
setsg = {1,2,3,4,5} #sets gabisa ada duplicate dan gabisa di order
print(setsg)
setsg.add(1)
print(setsg)#saat ini di print maka sets tidak akan menambahkan angka 1 karena sets tidak ingin duplikat

s = {'shiro', 'avan', 'arif'}
print(s)
s.add('adam') #function add untuk menambahkan pada set
print(s)
s.add('shiro')
print(s)#maka tidak akan bertambah

#kita juga bisa mengubah tuple menjadi set ataupun list menjadi sets

x = [1,1,2,2,3,3,4,4,5,5,6,6,7,7]
y = set(x) #fungsi untuk merubah tuple/list menjadi set
print(y)#maka tidak akan ada duplikat karena set tidak ingin duplikat

#kalian juga bisa mengubah sets ke tuple / list

f = list(y)
z = tuple(y)
print (f, z)

#diagram venn
#coba union
library_1 = {'harry potter', 'hunger games', 'maze runner'}
library_2 = {'maze runner', 'dilan 1990', 'dilan 1991'}

all_books_in_town = library_1.union(library_2) #gabisa pake add
print(all_books_in_town)

#coba intersection
at_both_libraries = library_2.intersection(library_1)
print(at_both_libraries)

difference_library1 = library_2.difference(library_1)
print(difference_library1)
difference_library2 = library_1.difference(library_2)
print(difference_library2)

