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
print([mantan + ' dumped me' for mantan in names])

#ps : keep ur personal life and work seperate man AHAHAHAHAHA
print(['i dumped ' + trash for trash in names]) #HEHEHEHEHEHEHEHE

#application on movies & rating
anime_rating = {"Overflow": 9, "Tokyo Ghoul" : 6, "Boku no Hero Academia" : 7, "Boku no Pico" : 2}

#dibawah ini adalah konten yang akan di sederhanain dengan comperhension
great_anime = []
for anime in anime_rating:
    #print(anime)
    #print(anime_rating[anime])
    if anime_rating[anime] < 3:
        great_anime.append(anime) 
print(great_anime)

#lalu dibawah ini disederhanain dengan comperhension
print([anime_bagus for anime_bagus in anime_rating if anime_rating[anime_bagus] < 3])