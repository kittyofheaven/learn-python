#list comperhensions
#bla bla bla ini di edit di web ngetes github commit
names = ['jennifer', 'jesselyn', 'susan', 'sophie']

#dibawah ini adalah konten yang akan di sederhanain dengan comperhension
l = []
for person in names:
    l.append(person)
print (l)

#klo dijadiin bahasa manusia kaya
#print 'orang' untuk setiap orang(<- ini variable) di names (<- ini list)
print ([orang for orang in names]) #ini nama comperhension ya gitulah

#bisa buat operation untuk setiap elemen didalam list

#dibawah ini adalah konten yang akan di sederhanain dengan comperhension
k = []
for ex in names:
    k.append(ex + ' dumped me')
print (k)

#lalu dibawah ini disederhanain dengan comperhension
print(mantan + ' dumped me' for mantan in names)
